# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:29:33 2023

@author: danis
"""
import os
import numpy as np
from manim import *
config.background_color = WHITE
config["background_color"] = WHITE

# Define the folder containing the .npy files
folder_path = r"C:\Users\danis\Desktop\MFG 598 Project\ManimProject\data\triton\npy"

# Triton has 3 nucleon clouds
red_coordinates = []
blue_coordinates = []
green_coordinates = []

N = 10 # points in each of the nucleon clouds
totFrame=501 # of npy files, time step
Npart=3 # Triton has 3 nucleon clouds

# Create a 3D array to store the coordinates of nucleons over time
coords=np.zeros((N*totFrame,Npart,3))

# Iterate over each time step (frame)
for i in range(totFrame):
    file_path = os.path.join(folder_path, f"{i}.npy")
    
    # Load the data from the .npy file
    data = np.load(file_path)
    
    # Iterate over each nucleon
    for j in range(N):
        # Iterate over each nucleon cloud (Npart)
        for k in range(Npart):
            # Extract and store the (x, y, z) coordinates of the nucleon
            coords[i*N+j,k,:]=data[j,k:k+3] # The slice k:k + 3 selects the elements from index (k, k+1, k+2)

# Create an empty array to store center of mass coordinates
cm=np.zeros((N*totFrame,3))

# Calculate center of mass for red, blue, and green particles
for i in range(N*totFrame):
    # Calculate center of mass for the nucleons at the current time step
    cm[i,:]=np.sum(coords[i,:,:],axis=0)/Npart
    # Recenter the coordinates by subtracting the center of mass
    coords[i,:,:]=coords[i,:,:]-cm[i,:]

# Separate coordinates into arrays for red, blue, and green particles
r=np.zeros((totFrame,N,3))
b=np.zeros((totFrame,N,3))
g=np.zeros((totFrame,N,3))

for i in range(3):
    # Extract and reshape coordinates for red, blue, and green particles
    r[:,:,i]=coords[:,0,i].reshape((totFrame,N))
    b[:,:,i]=coords[:,1,i].reshape((totFrame,N))
    g[:,:,i]=coords[:,2,i].reshape((totFrame,N))
    
class TritonAnimation(ThreeDScene):
    def construct(self):
        self.camera.frame_width = 50 # Adjust as needed
        self.camera.frame_height = 50  # Adjust as needed
        
        # Create paths for red, blue, and green particles
        red_paths = self.create_trajectory(r, color=RED)
        blue_paths = self.create_trajectory(b, color=BLUE)
        green_paths = self.create_trajectory(g, color=GREEN)
        
        # Create particles at their initial positions
        red_particles = [Sphere(radius=0.05, color=RED).move_to(r[0][i]).set_color(RED) for i in range(N)]
        blue_particles = [Sphere(radius=0.05, color=BLUE).move_to(b[0][i]).set_color(BLUE) for i in range(N)]
        green_particles = [Sphere(radius=0.05, color=GREEN).move_to(g[0][i]).set_color(GREEN) for i in range(N)]
        
        # Create AnimationGroup for simultaneous animation
        animations = AnimationGroup(*[
            MoveAlongPath(red_particles[i], red_paths[i])
            for i in range(N)
        ] + [
            MoveAlongPath(blue_particles[i], blue_paths[i])
            for i in range(N)
        ]+ [
            MoveAlongPath(green_particles[i], green_paths[i])
            for i in range(N)
        ], run_time=5, rate_func=linear)

        # Animate all particles simultaneously
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.play(animations)

    def create_trajectory(self, coords, color=BLUE_A):
        # Initialize an empty list to store the paths
        paths = []
        # Iterate over each particle
        for i in range(N):
            # Create a Vectorized Mobject representing the trajectory of the particle
            # set_points_smoothly is used to create a smooth trajectory from the given coordinates
            paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
        return paths
