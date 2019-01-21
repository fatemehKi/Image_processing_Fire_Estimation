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




