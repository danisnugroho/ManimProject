# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:55:39 2023

@author: danis
"""
import os
import numpy as np
from manim import *
config.background_color = WHITE
config["background_color"] = WHITE

# THIS FILE IS FOR PRE-TEST ONLY

'''
Examples:
# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen

# class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

#         square = Square()  # create a square
#         square.rotate(PI / 4)  # rotate a certain amount

#         self.play(Create(square))  # animate the creation of the square
#         self.play(Transform(square, circle))  # interpolate the square into the circle
#         self.play(FadeOut(square))  # fade out animation
'''

class TrajectoryAnimation(ThreeDScene):
    def construct(self):
        # Set the frame dimensions
        self.camera.frame_width = 12  # Adjust as needed
        self.camera.frame_height = 12  # Adjust as needed


        # Load the data from the file and split into coordinates
        data = np.genfromtxt('orbit.dat')
        particle1_coords = data[:, :3]  # x, y, z for particle 1
        particle2_coords = data[:, 3:]  # x, y, z for particle 2

        # Create paths for particles
        particle1_path = self.create_trajectory(particle1_coords)
        particle2_path = self.create_trajectory(particle2_coords)

        # Create particles at initial positions
        particle1 = Sphere(radius=0.2).move_to(particle1_coords[0]).set_color(BLUE)
        particle2 = Sphere(radius=0.2).move_to(particle2_coords[0]).set_color(RED)
        
        # Animate the trajectory
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.play(
            MoveAlongPath(particle1, particle1_path),
            MoveAlongPath(particle2, particle2_path),
            run_time=5,
            rate_func=linear
        )

        # Display the trajectories
        self.play(Create(particle1_path), Create(particle2_path))

    def create_trajectory(self, coords, color=BLUE_A):
        return VMobject().set_points_smoothly([*coords]).set_color(color)

 
# class DeuteronTest(ThreeDScene):
#     def construct(self):
#         # Set the frame dimensions
#         self.camera.frame_width = 25  # Adjust as needed
#         self.camera.frame_height = 25  # Adjust as needed
        
#         file_path = r"C:\Users\danis\Desktop\MFG 598 Project\ManimProject\data\deuteron\npy\0.npy" # Specify the path to the file you want to visualize
#         coords = np.load(file_path)
#         particle1_coords = coords[:, :3]  # x, y, z for particle 1
#         particle2_coords = coords[:, 3:]  # x, y, z for particle 2

#         # Calculate the center of mass (CM) for both particles
#         cm = 0.5 * (particle1_coords + particle2_coords)

#         # Recenter the coordinates by subtracting the CM
#         particle1_coords -= cm
#         particle2_coords -= cm

#         # Create paths for particles
#         particle1_path = self.create_trajectory(particle1_coords)
#         particle2_path = self.create_trajectory(particle2_coords)

#         # Create particles at initial positions
#         particle1 = Sphere(radius=0.2).move_to(particle1_coords[0]).set_color(BLUE)
#         particle2 = Sphere(radius=0.2).move_to(particle2_coords[0]).set_color(RED)

#         # Animate the trajectory and set the camera to focus on the particles
#         self.play(
#             MoveAlongPath(particle1, particle1_path),
#             MoveAlongPath(particle2, particle2_path),
#             run_time=5,
#             rate_func=linear
#         )
#         self.wait(1)  # Pause for 1 second to view the animation

#     def create_trajectory(self, coords, color=BLUE_A):
#         return VMobject().set_points_smoothly([*coords]).set_color(color)

# # Define the folder containing the .npy files
# folder_path = r"C:\Users\danis\Desktop\MFG 598 Project\ManimProject\data\deuteron\npy"
# red_coordinates = []
# blue_coordinates = []

# # Iterate through the .npy files in the folder
# for i in range(501):
#     file_path = os.path.join(folder_path, f"{i}.npy")
    
#     # Load the data from the .npy file
#     data = np.load(file_path)
    
#     # Take the first 10 rows for both nucleons (red and blue)
#     red_nucleon_coordinates = data[:10, :3]  # Columns 0, 1, and 2 for the red nucleon
#     blue_nucleon_coordinates = data[:10, 3:]  # Columns 3, 4, and 5 for the blue nucleon
    
#     # Append the coordinates to the respective output lists
#     red_coordinates.append(red_nucleon_coordinates)
#     blue_coordinates.append(blue_nucleon_coordinates)

# # Convert the lists of coordinates to NumPy arrays
# red_coordinates = np.array(red_coordinates)
# blue_coordinates = np.array(blue_coordinates)

# class DeuteronNotSimultaneous(ThreeDScene):
#     def construct(self):
#         # Set the frame dimensions
#         self.camera.frame_width = 75  # Adjust as needed
#         self.camera.frame_height = 75 # Adjust as needed

#         # Create paths for red and blue particles
#         red_paths = self.create_trajectory(red_coordinates, color=RED)
#         blue_paths = self.create_trajectory(blue_coordinates, color=BLUE)

#         # Create particles at their initial positions
#         red_particles = [Sphere(radius=0.05, color=RED).move_to(red_coordinates[0][i]) for i in range(10)]
#         blue_particles = [Sphere(radius=0.05, color=BLUE).move_to(blue_coordinates[0][i]) for i in range(10)]

#         # Animate the trajectory
#         self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
#         for i in range(10):
#             self.play(
#                 MoveAlongPath(red_particles[i], red_paths[i]),
#                 MoveAlongPath(blue_particles[i], blue_paths[i]),
#                 run_time=5,
#                 rate_func=linear
#             )

#     def create_trajectory(self, coords, color=BLUE_A):
#         paths = []
#         for i in range(10):
#             paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
#         return paths

# class DeuteronSimultaneous(ThreeDScene):
#     def construct(self):
#         # Set the frame dimensions
#         self.camera.frame_width = 75  # Adjust as needed
#         self.camera.frame_height = 75  # Adjust as needed

#         # Create paths for red and blue particles
#         red_paths = self.create_trajectory(red_coordinates, color=RED)
#         blue_paths = self.create_trajectory(blue_coordinates, color=BLUE)

#         # Create particles at their initial positions
#         red_particles = [Sphere(radius=0.05, color=RED).move_to(red_coordinates[0][i]) for i in range(10)]
#         blue_particles = [Sphere(radius=0.05, color=BLUE).move_to(blue_coordinates[0][i]) for i in range(10)]

#         # Create AnimationGroup for simultaneous animation
#         animations = AnimationGroup(*[
#             MoveAlongPath(red_particles[i], red_paths[i])
#             for i in range(10)
#         ] + [
#             MoveAlongPath(blue_particles[i], blue_paths[i])
#             for i in range(10)
#         ], run_time=5, rate_func=linear)

#         # Animate all particles simultaneously
#         self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
#         self.play(animations)

#     def create_trajectory(self, coords, color=BLUE_A):
#         paths = []
#         for i in range(10):
#             paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
#         return paths
    
# class DeuteronCenter(ThreeDScene):
#     def construct(self):
#         # Set the frame dimensions
#         self.camera.frame_width = 10  # Adjust as needed
#         self.camera.frame_height = 10  # Adjust as needed

#         # Calculate center of mass for red and blue particles
#         red_cm = np.mean(red_coordinates, axis=1)
#         blue_cm = np.mean(blue_coordinates, axis=1)

#         # Recenter the coordinates by subtracting the center of mass
#         red_coordinates_recentered = red_coordinates - red_cm[:, np.newaxis, :]
#         blue_coordinates_recentered = blue_coordinates - blue_cm[:, np.newaxis, :]

#         # Create paths for red and blue particles
#         red_paths = self.create_trajectory(red_coordinates_recentered, color=RED)
#         blue_paths = self.create_trajectory(blue_coordinates_recentered, color=BLUE)

#         # Create particles at their initial positions
#         red_particles = [Sphere(radius=0.05, color=RED).move_to(red_coordinates[0][i]).set_color(RED) for i in range(10)]
#         blue_particles = [Sphere(radius=0.05, color=BLUE).move_to(blue_coordinates[0][i]).set_color(BLUE) for i in range(10)]

#         # Create AnimationGroup for simultaneous animation
#         animations = AnimationGroup(*[
#             MoveAlongPath(red_particles[i], red_paths[i])
#             for i in range(10)
#         ] + [
#             MoveAlongPath(blue_particles[i], blue_paths[i])
#             for i in range(10)
#         ], run_time=5, rate_func=linear)

#         # Animate all particles simultaneously
#         self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
#         self.play(animations)

#     def create_trajectory(self, coords, color=BLUE_A):
#         paths = []
#         for i in range(10):
#             paths.append(VMobject().set_points_smoothly(coords[:, i, :]).set_color(color))
#         return paths