# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:07:51 2023

@author: danis
"""
import os
import numpy as np
import pandas as pd

from manim import *
config.background_color = WHITE
config["background_color"] = WHITE

# Define the folder containing the .csv files
folder_path = r"C:\Users\danis\Desktop\MFG 598 Project\ManimProject\data\alpha2"
# Alpha has 4 nucleon clouds
red_coordinates = []
blue_coordinates = []
green_coordinates = []
yellow_coordinates = []

N = 10 # points in each of the nucleon clouds
totFrame=1001 # of csv files, time step
Npart=4 # Alpha has 4 nucleon clouds

coords=np.zeros((N*totFrame,Npart,3))

# Iterate over each time step (frame)
for i in range(totFrame):
    file_path = os.path.join(folder_path, f"{i}.csv")
    
    # Load the data from the .csv file
    data = pd.read_csv(file_path, header=None).values
    # Iterate over each nucleon
    for j in range(N):
        # Iterate over each nucleon cloud (Npart)
        for k in range(Npart):
            # Extract and store the (x, y, z) coordinates of the nucleon
            coords[i*N+j,k,:]=data[j,k:k+3] # The slice k:k + 3 selects the elements from index (k, k+1, k+2)
            
cm=np.zeros((N*totFrame,3))
# Calculate center of mass for red, blue, green, and yellow particles
for i in range(N*totFrame):
    # Calculate center of mass for the nucleons at the current time step
    cm[i,:]=np.sum(coords[i,:,:],axis=0)/Npart
    # Recenter the coordinates by subtracting the center of mass
    coords[i,:,:]=coords[i,:,:]-cm[i,:]
# Separate coordinates into arrays for red, blue, green, and yellow particles    
r=np.zeros((totFrame,N,3))
b=np.zeros((totFrame,N,3))
g=np.zeros((totFrame,N,3))
y=np.zeros((totFrame,N,3))

for i in range(3):
    # Extract and reshape coordinates for red, blue, green, and yellow particles
    r[:,:,i]=coords[:,0,i].reshape((totFrame,N))
    b[:,:,i]=coords[:,1,i].reshape((totFrame,N))
    g[:,:,i]=coords[:,2,i].reshape((totFrame,N))
    y[:,:,i]=coords[:,3,i].reshape((totFrame,N))

class AlphaAnimation(ThreeDScene): # Class in Manim. This indicates that it's a 3D scene.
    def construct(self):
        # self.camera.frame_width = 20  # Adjust as needed
        # self.camera.frame_height = 20  # Adjust as needed
        
        # Create paths for red and blue particles
        red_paths = self.create_trajectory(r, color=RED)
        blue_paths = self.create_trajectory(b, color=BLUE)
        green_paths = self.create_trajectory(g, color=GREEN)
        yellow_paths = self.create_trajectory(y, color=YELLOW)
        
        # Create particles at their initial positions
        red_particles = [Sphere(radius=0.05,
        color=RED).move_to(r[0][i]).set_color(RED) for i in
        range(N)]
        blue_particles = [Sphere(radius=0.05,
        color=BLUE).move_to(b[0][i]).set_color(BLUE) for i in
        range(N)]
        green_particles = [Sphere(radius=0.05,
        color=GREEN).move_to(g[0][i]).set_color(GREEN) for i in
        range(N)]
        yellow_particles = [Sphere(radius=0.05,
        color=YELLOW).move_to(y[0][i]).set_color(YELLOW) for i
        in range(N)]
        
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
        ]+ [
            MoveAlongPath(yellow_particles[i], yellow_paths[i])
            for i in range(N)
        ], run_time=10, rate_func=linear)

        # Animate all particles simultaneously and rotate the camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.6)
        self.play(animations)


    def create_trajectory(self, coords, color=BLUE_A):
        paths = []
        # Iterate over each particle
        for i in range(N):
            # Create a Vectorized Mobject representing the trajectory of the particle
            # set_points_smoothly is used to create a smooth trajectory from the given coordinates
            paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
        return paths
