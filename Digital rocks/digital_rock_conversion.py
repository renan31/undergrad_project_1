# Importing libraries
import cv2
import numpy as np
import pandas as pd

# Reading the image file
data = np.fromfile("YOUR_IMAGE_FILE.RAW") # Input your image file

data = data.reshape(X_DIMENSION, Y_DIMENSION, Z_DIMENSION) # Input the dimensions of your file

data[np.isnan(data)] = -1
 
p = list()
for k in range(Z_DIMENSION):
    for j in range(Y_DIMENSION):
        for i in range(X_DIMENSION):
            if data[i,j,k] != -1:
                p.append(["C", i, j, k])

# Using NumPy to insert two new rows
n_grains = len(p) 
rock = np.array(p)
line_1 = [n_grains, None, None, None] # Number of grains
line_2 = [None, None, None, None] # Comments line
rock = np.r_[[line_2], rock]
rock = np.r_[[line_1], rock]

# Using Pandas to save the data into an xyz file
pd.DataFrame(rock).to_csv("rock.xyz", sep=" ", index=False, header=False)
