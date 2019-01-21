#author: fatemeh

import numpy as np
import imageio 
import matplotlib.pyplot as plt
from skimage import data

photo_data = imageio.imread('./Pictures/sd-3layers.jpg')
type(photo_data)

plt.figure(figsize=(15,15))
plt.imshow(photo_data)

photo_data.shape


#set a bar of pixel all to zero (creating a black bar)
photo_data[150:900, : ] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


#set a bar of pixel all to 255 (creating a white bar)
photo_data[150:900, : ] = 255
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

#filtering out all low values in the 
photo_data = imageio.imread('./Pictures/sd-3layers.jpg')
print("Shape of photo_data:", photo_data.shape)
low_value_filter = photo_data < 200
print("Shape of low_value_filter:", low_value_filter.shape)

plt.figure(figsize=(10,10))
plt.imshow(photo_data)
photo_data[low_value_filter] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data


