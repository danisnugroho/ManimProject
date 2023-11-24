# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 20:09:29 2023

@author: danis
"""
import os
import numpy as np
import pandas as pd

from manim import *
config.background_color = WHITE
config["background_color"] = WHITE

# Define the folder containing the .npy files
folder_path = r"C:\Users\danis\Desktop\MFG 598 Project\ManimProject\data\deuteron\csv"
red_coordinates = []
blue_coordinates = []

N = 10
totFrame=501
Npart=2

coords=np.zeros((N*totFrame,Npart,3))

for i in range(totFrame):
    file_path = os.path.join(folder_path, f"{i}.csv")
    
    # Load the data from the .csv file
    data = pd.read_csv(file_path, header=None).values
    
    for j in range(N):
        for k in range(Npart):
            coords[i*N+j,k,:]=data[j,k:k+3]

cm=np.zeros((N*totFrame,3))
# Calculate center of mass for red and blue particles
for i in range(N*totFrame):
    cm[i,:]=np.sum(coords[i,:,:],axis=0)/Npart
    coords[i,:,:]=coords[i,:,:]-cm[i,:]
    
r=np.zeros((totFrame,N,3))
b=np.zeros((totFrame,N,3))

for i in range(3):
    r[:,:,i]=coords[:,0,i].reshape((totFrame,N))
    b[:,:,i]=coords[:,1,i].reshape((totFrame,N))

class DeuteronAnimation(ThreeDScene):
    def construct(self):
        self.camera.frame_width = 30  # Adjust as needed
        self.camera.frame_height = 30  # Adjust as needed
        
        # Create paths for red and blue particles
        red_paths = self.create_trajectory(r, color=RED)
        blue_paths = self.create_trajectory(b, color=BLUE)

        # Create particles at their initial positions
        red_particles = [Sphere(radius=0.05, color=RED).move_to(r[0][i]).set_color(RED) for i in range(10)]
        blue_particles = [Sphere(radius=0.05, color=BLUE).move_to(b[0][i]).set_color(BLUE) for i in range(10)]

        # Create AnimationGroup for simultaneous animation
        animations = AnimationGroup(*[
            MoveAlongPath(red_particles[i], red_paths[i])
            for i in range(10)
        ] + [
            MoveAlongPath(blue_particles[i], blue_paths[i])
            for i in range(10)
        ], run_time=5, rate_func=linear)

        # Animate all particles simultaneously
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.play(animations)

    def create_trajectory(self, coords, color=BLUE_A):
        paths = []
        for i in range(10):
            paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
        return paths
