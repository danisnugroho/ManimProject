# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:36:05 2023

@author: danis
"""

import numpy as np
import os

# Load the data from the .npy file
stuff = np.load("npy/1.npy")

# Define the folder containing the .npy files
folder_path = "npy"
red_coordinates = []
blue_coordinates = []

# Iterate through the .npy files in the folder
for i in range(501):
    file_path = os.path.join(folder_path, f"{i}.npy")
    
    # Load the data from the .npy file
    data = np.load(file_path)
    
    # Take the first 10 rows for both nucleons (red and blue)
    red_nucleon_coordinates = data[:10, :3]  # Columns 0, 1, and 2 for the red nucleon
    blue_nucleon_coordinates = data[:10, 3:]  # Columns 3, 4, and 5 for the blue nucleon
    
    # Append the coordinates to the respective output lists
    red_coordinates.append(red_nucleon_coordinates)
    blue_coordinates.append(blue_nucleon_coordinates)

# Convert the lists of coordinates to NumPy arrays
red_coordinates = np.array(red_coordinates)
blue_coordinates = np.array(blue_coordinates)

# The red_coordinates and blue_coordinates arrays now contain the separated coordinates of red and blue nucleons.
print(red_coordinates.shape)  # This should print (501, 10, 3), indicating 501 time steps, 10 particles, and 3 coordinates for red nucleons.
print(blue_coordinates.shape)  # This should print (501, 10, 3), indicating 501 time steps, 10 particles, and 3 coordinates for blue nucleons.