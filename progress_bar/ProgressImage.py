import numpy as np
from PIL import Image
import sys
import subprocess
from png import ASCII_art_generator

class ProgressImage:
    def __init__(self, total, update_freq):
        self.total = total
        self.update_freq = update_freq
        rows, colomns = subprocess.check_output(['stty', 'size']).split()  # terminal size.
        self.rows = int(rows.decode("utf-8"))
        self.colomns = int(colomns.decode("utf-8"))
        ascii_art = ASCII_art_generator("fig1.png")
        shape = np.shape(ascii_art)
        for i in range(shape[1]):
            sys.stdout.write("x"*shape[0] + "\n")
    def update_progress_bar(self, progress):
        pass









if __name__ == "__main__":
    img = ProgressImage(100, 1)
