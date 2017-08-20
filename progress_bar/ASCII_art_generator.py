import numpy as np
from PIL import Image
import sys
import subprocess
from numba import jit

# @jit
def ASCII_art_generator(figname, max_shape):
    signs = np.array([ " ", ".", "-", "~", "+", "o", "0", "@" ])
    img = np.array(Image.open(figname).convert("RGBA"))
    img_BW = (img[:,:,0] + img[:,:,1] + img[:,:,2])//3    # Converting to Black/White
    shape = np.shape(img_BW)
    skips = np.array(shape)//np.array(max_shape)
    if skips[0] == 0 or skips[1] == 0:
        skips = np.array([1,1])
    reduced_shape = shape//(skips)

    # img_BW = np.array(img_BW / ((img[:,:,3]+1)/255.0), dtype=int)    # Including transparency information.
    # img2 = Image.fromarray(img_BW)
    # img2.save("image.png")
    max_color = np.max(img_BW)
    ascii_art = np.empty( shape=(reduced_shape), dtype=str)
    for i in range(reduced_shape[0]):
        for j in range(reduced_shape[1]):
            ascii_art[i,j] = signs[ int( (len(signs)-1)*img_BW[i*skips[0],j*skips[1]]/max_color) ]
    return ascii_art


if __name__ == "__main__":
    ascii_art = ASCII_art_generator("fig1.png", (80,160))
    shape = np.shape(ascii_art)
    for i in range(shape[0]):
        for j in range(shape[1]):
            sys.stdout.write(ascii_art[i,j])
        sys.stdout.write("\n")
