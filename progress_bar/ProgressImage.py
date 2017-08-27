import numpy as np
import os
from PIL import Image
import sys
import subprocess
import time
import curses
from ASCII_art_generator import ASCII_art_generator


class ProgressImage:
    def __init__(self, total, update_freq):
        self.total = total
        self.update_freq = update_freq
        rows, colomns = subprocess.check_output(['stty', 'size']).split()  # terminal size.
        self.rows = int(rows.decode("utf-8"))
        self.colomns = int(colomns.decode("utf-8"))
        shape = (self.colomns-10, self.rows-10)
        self.shape = shape
        self.size = self.rows*self.colomns
        self.ascii_art = ASCII_art_generator("fig1.png", shape, return_as="string")
        # self.img_buffer = ( (" "*shape[0] + "\n")*shape[1] )
        # sys.stdout.write(self.img_buffer)
        # sys.stdout.flush()

        self.stdscr = curses.initscr()

    def update_progress_bar(self, progress):
        # remaining_indexes = np.arange(0, self.size-1)
        # chosen_index =
        index = ((progress*self.size) + self.total//2 )//self.total
        self.img_buffer = self.ascii_art[0:index] + " "*(self.size-index)
        self.stdscr.addstr(0, 0, self.ascii_art)
        self.stdscr.refresh()







if __name__ == "__main__":
    img = ProgressImage(100, 1)
    for i in xrange(1,101):
        img.update_progress_bar(i)
        time.sleep(0.1)
