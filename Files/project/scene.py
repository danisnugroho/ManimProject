# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:55:39 2023

@author: danis
"""
import numpy as np
from manim import *
config.background_color = WHITE
config["background_color"] = WHITE

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

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