# :ghost: Welcome to PySpy :ghost:
The purpose of PySpy is to create a realistic keylogger for educational purposes</br></br>
After working for NASA :rocket: and performing pen-testing for them, I knew I wanted to challenge myself and learn within the cybersecurity field. I knew about famour hackers using keyloggers, but never really understood how a program like that would work. So...</br>
***I decided to build one!***

## Warning
This program is by no means intended to be used in the field, and I take no responsibility for your actions using this program for any malicious reasons. Please be *smart* and *safe* while using this program. Have fun and run it on your own computer, but respect the privacy of others.

## How to use
Prior to running this script, you will need two things:
1. create a ***"format.txt"*** file in the same directory that the script is contained within. The file will need to be structured as follows:
``` txt
<senders-email>
<recievers-email>
```
2. You will need to import yagmail and run the following python code with the sender email and password:
```python
import yagmail
yagmail.register('mygmailusername', 'mygmailpassword')
```
Currently, the script works by running the following command on your favorite bash terminal </br>
```shell
sudo python installer.py
```
The key here is that you need **ROOT** access to be able to retrieve the on_press events from the keyboard. So, if you were going to use this in real life you would need some form of root escalation prior to running this script.

## What to expect from PySpy
PySpy will track the users :keyboard: and log the keystrokes to a file until the application is terminated. Every time interval, an email will be sent to the recipient email containing the updated log file that is timestamped. The time interval for emailing can be set by updating the email object creation within **installer.py**. If you plan on not DOSing your own email, I would recommend increasing the time to 10 minutes (keep in mind it's tracked in seconds so multiply by 60 for mins).

## Future improvements
Be on the lookout for screenshot capabilites. I am hoping to have this completed by the end of the week.
