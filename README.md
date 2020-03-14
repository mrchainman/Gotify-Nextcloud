# Gotify-Nextcloud

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)  

A Python script that fetches notifications from the Nextcloud notification API and pushes them to a Gotify server.

The code is mostly based on [Talkify](https://github.com/mrchainman/Talkify), which was the old version of this project, that used the Talk specific API.

### Usage

Just adapt the settings in the settings.py file and start run the script.
A working Nextcloud instance and a working Gotify setup is needed.

### TODO

- [ ] Find a better way for authentication, as username and password are stored in plaintext in the settings.py file
- [ ] Use a persistent storage so that old notifications aren't resent, when the script is restarted
