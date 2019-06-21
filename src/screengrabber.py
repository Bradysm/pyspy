# file used to define screenshot capabilities

import pyscreenshot as Camera

class ImageGrabber:
    """
    Imagegrabber for computers. Gives users the funcitonality
    to take screenshots of the computer screen in various ways.
    """
    def grab_to_file(self, filename="screenshot.png"):
        """
        Takes screenshot of the screen and saves it to the given filename
        return: Image object
        """
        img = Camera.grab()
        img.save(filename)
        return img
    
    def grab_and_show(self, filename="screenshot.png"):
        """
        Takes screenshot of the screen and saves it to the given filename.
        Once file is saved, the image is displayed on the screen
        return: Image object
        """
        img = self.grab_to_file(filename)
        img.show()
        

