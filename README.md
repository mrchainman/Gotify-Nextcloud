# Gotify-Nextcloud

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

## IMPORTANT: Since there are https://github.com/Andrewerr/NextcloudServices and https://github.com/nextcloud/notify_push now, this project is no longer needed.
## I will neither MAINTAIN the project, nor guarantee for onwards COMPATABILITY.
## If you feel a need for this project, you are free to fork and change it as needed.

A Python script that fetches notifications from the Nextcloud notification API and pushes them to a Gotify server.



### Usage

Just adapt the settings in the settings.py file and start run the script.
A working Nextcloud instance and a working Gotify setup is needed.

### Tips
- You can setup logging, by providing the path to a logfile in settings.py
- To use the provided servicefile, copy it to /etc/systemd/system and enable/start it. (To use it, push_msg.py must be located in /usr/local/bin/

### TODO

- [ ] Find a better way for authentication, as username and password are stored in plaintext in the settings.py file
- [ ] Use a persistent storage so that old notifications aren't resent, when the script is restarted
