import numpy as np
import Image
import sys
import subprocess

signs = np.array([ " ", ".", "" "-", "~", "+", "o", "0", "@" ])

img = np.array(Image.open("fig3.png").convert("RGBA"))
img_BW = (img[:,:,0] + img[:,:,1] + img[:,:,2])/3    # Converting to Black/White
shape = np.shape(img_BW)
print shape
# img_BW = np.array(img_BW / ((img[:,:,3]+1)/255.0), dtype=int)    # Including transparency information.
# img2 = Image.fromarray(img_BW)
# img2.save("image.png")

max_color = np.max(img_BW)
ascii_art = np.empty(shape, dtype=str)
for i in range(shape[0]):
    for j in range(shape[1]):
        ascii_art[i,j] = signs[ int( (len(signs)-1)*img_BW[i,j]/max_color) ]
for i in range(0, shape[0], shape[0]/70):
    for j in range(0, shape[1], shape[0]/130):
        sys.stdout.write(ascii_art[i,j])
    sys.stdout.write("\n")
