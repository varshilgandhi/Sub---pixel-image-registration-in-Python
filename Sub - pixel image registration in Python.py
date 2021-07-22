# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:40:20 2021

@author: abc
"""

"""

Sub - pixel image registration in Python
 
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage import data, io
from skimage.feature import register_translation
#from skimage.feature.register_translation import _upsampled_dft
from scipy.ndimage import fourier_shift

#read our images
image = io.imread("BSE.jpg")
offset_image = io.imread("BSE_transl.jpg")

#offset image translated by (-17.45, 18.75) in y and x

#define sub-pixel registration 
shifted, error, diffphase = register_translation(image, offset_image, 100)
print(f"detected subpixel (y,x): {shifted}")

#Let's correct our offset image using shift filter of scipy
from scipy.ndimage import shift
corrected_image = shift(offset_image, shift=(shifted[0], shifted[1]), mode='constant')

#Let's plot all the images
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap="gray")
ax1.title.set_text('Input image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(offset_image, cmap='gray')
ax2.title.set_text('Offset image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(corrected_image, cmap="gray")
ax3.title.set_text('Corrected')
plt.show()



 


