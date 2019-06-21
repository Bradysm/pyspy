# :ghost: Welcome to PySpy :ghost:
The purpose of PySpy is to create a realistic keylogger for educational purposes</br></br>
After working for NASA :rocket: and performing pen-testing for them, I knew I wanted to challenge myself and learn within the cybersecurity field. I knew about famous hackers using keyloggers, but never really understood how a program like that would work. So...</br>
***I decided to build one!***

## :rotating_light: WARNING :rotating_light:
This program is by no means intended to be used in the field, and I take no responsibility for your actions using this program for any malicious reasons. Please be *smart* and *safe* while using this program. Have fun and run it on your own computer, but respect the privacy of others.

## How to use
Prior to running this script, you will need two things:
1. create a ***"format.txt"*** file in the src directory. The file will need to be structured as follows:
``` txt
<senders-email>
<recievers-email>
```
2. You will then need to make sure that pyspy.sh has executable rights:
```bash
chmod +x pyspy.sh
```
Currently, the script works by running the following command on your favorite bash terminal </br>
```shell
./pyspy.sh
```
This will run the keylogger and install the dependencies that are needed to run the program. It will aslo setup the email keyring so you don't have to!</br>
The key here is that you need **ROOT** access to be able to retrieve the on_press events from the keyboard. So, if you were going to use this in real life you would need some form of root escalation prior to running this script.

## What to expect from PySpy :snake: :keyboard:
PySpy will track the users :keyboard: and log the keystrokes to a file until the application is terminated. Every time interval, an email will be sent to the recipient email containing the updated log file that is timestamped and a :camera: snapshot of the current screen! The time interval for emailing can be set by updating the email object creation within **installer.py**. If you plan on not DOSing your own email, I would recommend increasing the time to 10 minutes (keep in mind it's tracked in seconds so multiply by 60 for mins).
