
#!/usr/bin/env python3

import requests
import json
import time
import logging
try:
    from settings import *
except:
    print("Please provide a settings.py file")
    exit(0)


# Setup logging.
try:
    if log_file:
        logging.basicConfig(
                filename=log_file,
                filemode='a',
                level=logging.INFO,
                format='%(asctime)s %(levelname)8s - %(message)s'
        )
except FileNotFoundError:
    print("ERROR: Invalid log file path specified in settings.py")
    exit(0)
except NameError:
    # log_file is an optional, setting and may not be present in older config files
    pass


# set nextcloud header
headers = {'OCS-APIRequest': 'true',
           'Content-Type': 'application/json',
           'Accept': 'application/json'
           }

# set gotify header
headerspush = {'X-Gotify-Key': token}

# create empty messages list
# TODO: Could we somehow replace the list with a generator to improve speed?
notifications = []


def get_notifications():
    """Retrieve notifications from nextcloud"""
    try:
        # retrieve json data from the notifications endpoint
        r = requests.get(url, headers=headers, auth=(user, pw))
        # load the json data
        m = (r.json())
        if r.status_code < 300:
            # only handle success status codes
            return m["ocs"]["data"]
        else:
            logging.error('failed to retrieve notifications - %s', r.text)
    except requests.exceptions.RequestException as err:
        logging.info("failed to connect to nextcloud - %s", repr(err))
    except (ValueError, KeyError) as err:
        logging.error("failed to parse notifications - %s", repr(err))
    return []


def push_notification(notification_id, date, title, msg, priority):
    """Send the notification to the gotify server."""
    try:
        response = requests.post(
                urlpush,
                headers=headerspush,
                data={
                    'id': notification_id,
                    'date': date,
                    'title': title,
                    'message': msg,
                    'priority': priority}
        )
    except requests.exceptions.RequestException as e:
        logging.error("push to gotify server failed - %s", repr(e))
        return False

    if response.status_code < 300:
        return True
    else:
        logging.error("push to gotify server failed with HTTP status %s - %s", response.status_code, response.text)
        return False


# start infinite loop for listening
if __name__ == "__main__":
    while True:
        new_notification_list = get_notifications()

        # Iterate over the notifications
        for n in new_notification_list:
            try:
                n_id  = n["notification_id"]  # id
                title = n["subject"]
                date  = n["datetime"]
                msg   = n["message"] or " "
            except (KeyError, AttributeError):
                # invalid or unsupported notification format
                logging.warning('Invalid notification object - %s', n)
                continue

            # check if message was already pushed
            if n_id is None or n_id in notifications:
                continue

            # else send push notification
            if push_notification(n_id, date, title, msg, notification_priority):
                # Add the message to the list if successfully pushed to the Gotify server
                notifications.append(n_id)

        # wait before checking again
        time.sleep(delay)
