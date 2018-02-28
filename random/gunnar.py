from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

image = misc.imread("image.png")
image = np.array(image)
image = image[21:535,105:1030]
misc.imsave("new_image.png",image)

image = misc.imread("new_image.png")
image = np.swapaxes(image, 0, 1)
shape = np.shape(image)
s=0
values = np.zeros(np.shape(image)[0])
for i in range(np.shape(image)[0]):
	for j in range(np.shape(image)[1]):
		if ((np.array([0,0,200]) <= image[i,j]).all() and (image[i,j] <= np.array([200,200,255])).all()):
			#print(image[i,j])
			values[i] = shape[1] - j
			s += 1
			break

result = np.sum(values) *7.0/shape[0] *18000.0/shape[1]
print(result)
print(shape)
print(s)
plt.plot(values)
plt.show()