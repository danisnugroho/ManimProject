# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:11:05 2023

@author: danis
"""
import os
import numpy as np
from manim import *
config.background_color = WHITE
config["background_color"] = WHITE

folder_path = "alpha"
red_coordinates = []
blue_coordinates = []
green_coordinates = []
yellow_coordinates = []

N = 10
totFrame=1000
Npart=4

coords=np.zeros((N*totFrame,Npart,3))

for i in range(totFrame):
    file_path = os.path.join(folder_path, f"{i}.npy")
    
    # Load the data from the .npy file
    data = np.load(file_path)
    
    for j in range(N):
        for k in range(Npart):
            coords[i*N+j,k,:]=data[j,k:k+3]
    
'''
    # Take the first 10 rows for three nucleons (red, blue, and green)
    red_nucleon_coordinates = data[:N, :3]  # Columns 0, 1, and 2 for the red nucleon
    blue_nucleon_coordinates = data[:N, 3:6]  # Columns 3, 4, and 5 for the blue nucleon
    green_nucleon_coordinates = data[:N, 6:9]  # Columns 6, 7, and 8 for the green nucleon
    yellow_nucleon_coordinates = data[:N, 9:]  # Columns 9, 10, and 11 for the green nucleon
    
    # Append the coordinates to the respective output lists
    red_coordinates.append(red_nucleon_coordinates)
    blue_coordinates.append(blue_nucleon_coordinates)
    green_coordinates.append(green_nucleon_coordinates)
    yellow_coordinates.append(yellow_nucleon_coordinates)
'''    

cm=np.zeros((N*totFrame,3))
for i in range(N*totFrame):
    cm[i,:]=np.sum(coords[i,:,:],axis=0)/Npart
    coords[i,:,:]=coords[i,:,:]-cm[i,:]
#red_coordinates=coords[:,0,:]

# Convert the lists of coordinates to NumPy arrays
#red_coordinates = np.array(red_coordinates)
#blue_coordinates = np.array(blue_coordinates)
#green_coordinates = np.array(green_coordinates)
#yellow_coordinates = np.array(yellow_coordinates)

r=np.zeros((totFrame,N,3))
b=np.zeros((totFrame,N,3))
g=np.zeros((totFrame,N,3))
y=np.zeros((totFrame,N,3))
for i in range(3):
    r[:,:,i]=coords[:,0,i].reshape((totFrame,N))
    b[:,:,i]=coords[:,1,i].reshape((totFrame,N))
    g[:,:,i]=coords[:,2,i].reshape((totFrame,N))
    y[:,:,i]=coords[:,3,i].reshape((totFrame,N))


class AlphaAnimation(ThreeDScene):
    def construct(self):
        # Set the frame dimensions
        self.camera.frame_width = 10  # Adjust as needed
        self.camera.frame_height = 10  # Adjust as needed

        ## Calculate center of mass
        #red_cm = np.mean(red_coordinates, axis=1)
        #blue_cm = np.mean(blue_coordinates, axis=1)
        #green_cm = np.mean(green_coordinates, axis=1)
        #yellow_cm = np.mean(yellow_coordinates, axis=1)
        #
        ## Recenter the coordinates by subtracting the center of mass
        #red_coordinates_recentered = red_coordinates - red_cm[:, np.newaxis, :]
        #blue_coordinates_recentered = blue_coordinates - blue_cm[:, np.newaxis, :]
        #green_coordinates_recentered = green_coordinates - green_cm[:, np.newaxis, :]
        #yellow_coordinates_recentered = yellow_coordinates - yellow_cm[:, np.newaxis, :]
        
        # Create paths for red and blue particles
        red_paths = self.create_trajectory(r, color=RED)
        blue_paths = self.create_trajectory(b, color=BLUE)
        green_paths = self.create_trajectory(g, color=GREEN)
        yellow_paths = self.create_trajectory(y, color=YELLOW)
        
        # Create particles at their initial positions
        red_particles = [Sphere(radius=0.05,
        color=RED).move_to(red_coordinates[0][i]).set_color(RED) for i in
        range(N)]
        blue_particles = [Sphere(radius=0.05,
        color=BLUE).move_to(blue_coordinates[0][i]).set_color(BLUE) for i in
        range(N)]
        green_particles = [Sphere(radius=0.05,
        color=GREEN).move_to(green_coordinates[0][i]).set_color(GREEN) for i in
        range(N)]
        yellow_particles = [Sphere(radius=0.05,
        color=YELLOW).move_to(yellow_coordinates[0][i]).set_color(YELLOW) for i
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
        ], run_time=5, rate_func=linear)

        # Animate all particles simultaneously
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.play(animations)

    def create_trajectory(self, coords, color=BLUE_A):
        paths = []
        for i in range(N):
            paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
        return paths
