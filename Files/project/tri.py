# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:44:04 2023

@author: danis
"""
import os
import numpy as np
from manim import *

# Change background color
config.background_color = WHITE
config["background_color"] = WHITE

folder_path = r"C:\Users\danis\Desktop\MFG 598 Project\ManimProject\data\triton\npy"

# Triton has 3 nucleon clouds
red_coordinates = []
blue_coordinates = []
green_coordinates = []

# Iterate through the .npy files in the folder
for i in range(501):
    file_path = os.path.join(folder_path, f"{i}.npy")
    
    # Load the data from the .npy file
    data = np.load(file_path)
    
    # Take the first 10 rows for both nucleons (red, blue, and green)
    red_nucleon_coordinates = data[:10, :3]  # Columns 0, 1, and 2 for the red nucleon
    blue_nucleon_coordinates = data[:10, 3:6]  # Columns 3, 4, and 5 for the blue nucleon
    green_nucleon_coordinates = data[:10, 6:]  # Columns 3, 4, and 5 for the blue nucleon
    
    # Append the coordinates to the respective output lists
    red_coordinates.append(red_nucleon_coordinates)
    blue_coordinates.append(blue_nucleon_coordinates)
    green_coordinates.append(green_nucleon_coordinates)
    
# Convert the lists of coordinates to NumPy arrays
red_coordinates = np.array(red_coordinates)
blue_coordinates = np.array(blue_coordinates)
green_coordinates = np.array(green_coordinates)

class TritonAnimation(ThreeDScene):
    def construct(self):
        # Set the frame dimensions
        self.camera.frame_width = 10  # Adjust as needed
        self.camera.frame_height = 10  # Adjust as needed

        # Calculate center of mass
        red_cm = np.mean(red_coordinates, axis=1)
        blue_cm = np.mean(blue_coordinates, axis=1)
        green_cm = np.mean(green_coordinates, axis=1)
        
        # Recenter the coordinates by subtracting the center of mass
        red_coordinates_recentered = red_coordinates - red_cm[:, np.newaxis, :]
        blue_coordinates_recentered = blue_coordinates - blue_cm[:, np.newaxis, :]
        green_coordinates_recentered = green_coordinates - green_cm[:, np.newaxis, :]
        
        # Create paths for red and blue particles
        red_paths = self.create_trajectory(red_coordinates_recentered, color=RED)
        blue_paths = self.create_trajectory(blue_coordinates_recentered, color=BLUE)
        green_paths = self.create_trajectory(green_coordinates_recentered, color=GREEN)
        
        # Create particles at their initial positions
        red_particles = [Sphere(radius=0.05, color=RED).move_to(red_coordinates[0][i]).set_color(RED) for i in range(10)]
        blue_particles = [Sphere(radius=0.05, color=BLUE).move_to(blue_coordinates[0][i]).set_color(BLUE) for i in range(10)]
        green_particles = [Sphere(radius=0.05, color=GREEN).move_to(green_coordinates[0][i]).set_color(GREEN) for i in range(10)]
        
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
        # Initialize an empty list to store the paths
        paths = []
        # Iterate over each particle
        for i in range(10):
            # Create a Vectorized Mobject representing the trajectory of the particle
            # set_points_smoothly is used to create a smooth trajectory from the given coordinates
            paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
        return paths