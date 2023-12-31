# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:31:30 2023

@author: danis
"""

import numpy as np
import os

content = np.load("npy/0.npy")

folder_path = "npy"
red_coordinates = []
blue_coordinates = []
green_coordinates = []

for i in range(501):
    file_path = os.path.join(folder_path, f"{i}.npy")
    
    # Load the data from the .npy file
    data = np.load(file_path)
    
    # Take the first 10 rows for three nucleons (red, blue, and green)
    red_nucleon_coordinates = data[:10, :3]  # Columns 0, 1, and 2 for the red nucleon
    blue_nucleon_coordinates = data[:10, 3:6]  # Columns 3, 4, and 5 for the blue nucleon
    green_nucleon_coordinates = data[:10, 6:]  # Columns 6, 7, and 8 for the green nucleon
    
    # Append the coordinates to the respective output lists
    red_coordinates.append(red_nucleon_coordinates)
    blue_coordinates.append(blue_nucleon_coordinates)
    green_coordinates.append(green_nucleon_coordinates)
    
# Convert the lists of coordinates to NumPy arrays
red_coordinates = np.array(red_coordinates)
blue_coordinates = np.array(blue_coordinates)
green_coordinates = np.array(green_coordinates)