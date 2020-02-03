#!/usr/bin/python3
import requests
import json
import time
from settings import *

# set nextcloud header
headers = {'OCS-APIRequest': 'true',
           'Content-Type': 'application/json',
           'Accept': 'application/json'
          }

# set gotify header
headerspush = {'X-Gotify-Key': token}

# create empty messages list
messages = []

# start infinite loop for listening
while True:
    # retrieve json data from talk app
    r = requests.get(url, headers=headers, auth=(user, pw))
    # load the json data
    m = (r.json())
    # Iterate through the conversations
    for i in range(len(m["ocs"]["data"])):
        # Parse who send the message
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
            # Add the message to the list
            messages.append(msg)
    # wait 5 seconds
    time.sleep( 5 )
