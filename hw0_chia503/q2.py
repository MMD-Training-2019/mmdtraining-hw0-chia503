# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:25:25 2019

@author: User
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image=Image.open('sumi.jpg')
arr=np.array(image)
arr=arr/2
plt.imsave('Q2.jpg',arr.astype(np.uint8))