# Importing libraries 
import cv2
import numpy as np
import pandas as pd

# Reading the image file
data = np.fromfile("YOUR_FILE.RAW")  # Input your file
data = data.reshape("X_DIMENSION","Y_DIMENSION","Z_DIMENSION") # Input the dimensions of your file's sample
data[np.isnan(data)] = -1
p = list()
for k in range("Z_DIMENSION"):
    for j in range("Y_DIMENSION"):
        for i in range("X_DIMENSION"):
            if data[i,j,k] != -1:
                p.append([i, j, k])
            
# Importing p as a Pandas dataframe
rock = pd.DataFrame(p, columns=["x", "y", "z"])

# Adding a new column (of "atoms", from the structure of .xyz files, here I used carbon but you can use any atom of your choice) 
rock["atom"] = "C"
columns = ["atom", "x", "y", "z"]
rock = rock[columns]

# Saving the dataframe as an .xyz file
rock.to_csv("rock.xyz", sep = " ", index = False, header = False)
