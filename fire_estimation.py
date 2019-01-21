#author: fatemeh

import numpy as np
import imageio 
import matplotlib.pyplot as plt
from skimage import data
import random

photo_data = imageio.imread('./Pictures/sd-3layers.jpg')
type(photo_data)

plt.figure(figsize=(15,15))
plt.imshow(photo_data)

photo_data.shape


################set a bar of pixel all to zero (creating a black bar)
photo_data[150:900, : ] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


################set a bar of pixel all to 255 (creating a white bar)
photo_data[150:900, : ] = 255
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

###############filtering out all low values in the image and making them all black (zero)
photo_data = imageio.imread('./Pictures/sd-3layers.jpg')
print("Shape of photo_data:", photo_data.shape)
low_value_filter = photo_data < 200
print("Shape of low_value_filter:", low_value_filter.shape)
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
photo_data[low_value_filter] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

###############creating a while diagonal line in the image
rows_range = np.arange(len(photo_data))
cols_range = rows_range
print(type(rows_range))
photo_data[rows_range, cols_range] = 255
plt.figure(figsize=(15,15))
plt.imshow(photo_data)
           
#############creating a circle mask out of the image
total_rows, total_cols, total_layers = photo_data.shape
#print("photo_data = ", photo_data.shape)
X, Y = np.ogrid[:total_rows, :total_cols]
#print("X = ", X.shape, " and Y = ", Y.shape)
center_row, center_col = total_rows / 2, total_cols / 2
#print("center_row = ", center_row, "AND center_col = ", center_col)
#print(X - center_row)
#print(Y - center_col)
dist_from_center = (X - center_row)**2 + (Y - center_col)**2
#print(dist_from_center)
radius = (total_rows / 2)**2
#print("Radius = ", radius)
circular_mask = (dist_from_center > radius)
#print(circular_mask)
print(circular_mask[1500:1700,2000:2200])
photo_data = imageio.imread('./Pictures/sd-3layers.jpg')
photo_data[circular_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)
