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
folder_path = "alpha"
red_coordinates = []
blue_coordinates = []
green_coordinates = []

N = 10
totFrame=1000
Npart=3

coords=np.zeros((N*totFrame,Npart,3))

for i in range(totFrame):
    file_path = os.path.join(folder_path, f"{i}.npy")
    
    # Load the data from the .npy file
    data = np.load(file_path)
    
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
g=np.zeros((totFrame,N,3))

for i in range(3):
    r[:,:,i]=coords[:,0,i].reshape((totFrame,N))
    b[:,:,i]=coords[:,1,i].reshape((totFrame,N))
    g[:,:,i]=coords[:,2,i].reshape((totFrame,N))
    
class TritonAnimation(ThreeDScene):
    def construct(self):
        
        # Create paths for red and blue particles
        red_paths = self.create_trajectory(r, color=RED)
        blue_paths = self.create_trajectory(b, color=BLUE)
        green_paths = self.create_trajectory(g, color=GREEN)
        
        # Create particles at their initial positions
        red_particles = [Sphere(radius=0.05, color=RED).move_to(r[0][i]).set_color(RED) for i in range(10)]
        blue_particles = [Sphere(radius=0.05, color=BLUE).move_to(b[0][i]).set_color(BLUE) for i in range(10)]
        green_particles = [Sphere(radius=0.05, color=GREEN).move_to(g[0][i]).set_color(GREEN) for i in range(10)]
        
        # Create AnimationGroup for simultaneous animation
        animations = AnimationGroup(*[
            MoveAlongPath(red_particles[i], red_paths[i])
            for i in range(10)
        ] + [
            MoveAlongPath(blue_particles[i], blue_paths[i])
            for i in range(10)
        ]+ [
            MoveAlongPath(green_particles[i], green_paths[i])
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
