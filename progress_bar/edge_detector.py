import numpy as np
from PIL import Image
from ASCII_art_generator import reduce_img, ASCII_art_generator

def RGBA_distance(RGBA_array1, RGBA_array2):
    # distance = np.sum(abs(RGBA_array2 - RGBA_array1))
    # distance = np.sum(abs(RGBA_array2[3] - RGBA_array1[3]))
    distance = np.sum(abs(RGBA_array2[0:3] - RGBA_array1[0:3]))
    return distance 

def show_edge_plot(edge_img_array):
    signs = np.array([" ", "_", "|", "/", "\\" ])
    shape = np.shape(edge_img_array)
    edge_art = ""
    for i in range(shape[0]):
        for j in range(shape[1]):
            edge_art += signs[edge_img_array[i,j]]
        edge_art += "\n"
    return edge_art

img_array = reduce_img("fig1.png", (40,80))
img_shape = np.shape(img_array[:,:,0])
edge_img_array = np.zeros(img_shape,dtype=int)

check_distance = 1
check_tolerance = 200
diagonal_check_modifier = 1.7


for i in range(img_shape[0]-check_distance):
    for j in range(img_shape[1]):
        if RGBA_distance( img_array[i,j], img_array[i+check_distance,j] ) > check_tolerance:           
            edge_img_array[i,j] = 1

for i in range(img_shape[0]):
    for j in range(img_shape[1]-check_distance):
        if RGBA_distance( img_array[i,j], img_array[i,j+check_distance] ) > check_tolerance:
            edge_img_array[i,j] = 2

for i in range(img_shape[0]-check_distance):
    for j in range(img_shape[1]-check_distance):
        if RGBA_distance( img_array[i,j], img_array[i+check_distance,j+check_distance] ) > check_tolerance*diagonal_check_modifier:
            edge_img_array[i,j] = 3

for i in range(img_shape[0]-check_distance):
    for j in range(img_shape[1]-check_distance):
        if RGBA_distance( img_array[i,j], img_array[i+check_distance,j-check_distance] ) > check_tolerance*diagonal_check_modifier:
            edge_img_array[i,j] = 4


edge_img_str = show_edge_plot(edge_img_array)

print(edge_img_str)

