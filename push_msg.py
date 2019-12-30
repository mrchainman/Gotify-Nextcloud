#!/usr/bin/python3
import requests
import json
import time

# set nextcloud variables
url = 'https://cloud.example.com/ocs/v2.php/apps/spreed/api/v1/room'
user = 'username'
pw = 'password'
# set header
headers = {'OCS-APIRequest': 'true',
           'Content-Type': 'application/json',
           'Accept': 'application/json'
          }
# create empty messages list
messages = []

# set gotify variables
urlpush = 'gotify-url'
token = 'gotify-app-token'
headerspush = {'X-Gotify-Key': token}

# start infinite loop for listening
while True:
    # retrieve json data from talk app
    r = requests.get(url, headers=headers, auth=(user, pw))
    m = (r.json())
    # iterate through conversations, numbers must be specified manually at
    # the moment, this is for the case of 3 conversations.
    for i in 0,1,2:
        who = m["ocs"]["data"][i]["lastMessage"]["actorDisplayName"]
        msg = m["ocs"]["data"][i]["lastMessage"]["message"]
        # check if message was already pushed
        if msg in messages:
            continue
        # check if I wrote the message
        elif who == "Your Name":
            continue
        # else send push notification
        else:
            requests.post(urlpush, headers=headerspush, data={'title': who, 'message': msg, 'priority': '10'})
            messages.append(msg)
    # wait 5 seconds
    time.sleep( 5 )
