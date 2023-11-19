# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:42:11 2023

@author: danis
"""
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file (replace 'data_file.csv' with the actual file name)
data = np.genfromtxt('orbit.dat')

# Split the data into coordinates for each particle
particle1_x, particle1_y = data[:, 0], data[:, 1]
particle2_x, particle2_y = data[:, 3], data[:, 4]

# Plot the trajectories
plt.figure(figsize=(8, 8))
plt.plot(particle1_x, particle1_y, label='Particle 1')
plt.plot(particle2_x, particle2_y, label='Particle 2')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Trajectories of Particles')
plt.legend()
plt.grid(True)
plt.show()
