
class Keylogger:
    """
    Keylogger provides the functionality for a keylogger
    Can be used in applications to SPY on peoples compyters
    and obtain passwords and screenshots
    """
    def __init__(self, filename="~/Documents/log.txt", email="default@gmail.com", pswd="drowssap"):
        self.email = email
        self.pswd = pswd
        self.mem = []
        self.fname = filename

    def __screenshot(self):
        # TODO takes a screenshot of the persons screen
        return None

    def __get_key(self):
        # TODO gets the key that was pressed and returns the character
        return None

    def __log_key(self):
        # TODO logs the key into the memory, and writes to file at maxsize
        return None

    def run_keylogger(self):
        # TODO runs keylogger logic
        print("running")