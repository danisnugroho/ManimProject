# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:55:39 2023

@author: danis
"""
import numpy as np
from manim import *


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

class TrajectoryAnimation(Scene):
    def construct(self):
        # Set the frame dimensions
        self.camera.frame_width = 12  # Adjust as needed
        self.camera.frame_height = 12  # Adjust as needed
        
        # Create a white rectangle to serve as the background
        background = Rectangle(width=12, height=12, fill_color=WHITE, fill_opacity=1).shift(ORIGIN)


        # Load the data from the file and split into coordinates
        data = np.genfromtxt('orbit.dat')
        particle1_coords = data[:, :3]  # x, y, z for particle 1
        particle2_coords = data[:, 3:]  # x, y, z for particle 2

        # Create paths for particles
        particle1_path = self.create_trajectory(particle1_coords)
        particle2_path = self.create_trajectory(particle2_coords)

        # Create particles at initial positions
        particle1 = Dot(color=BLUE).move_to(particle1_coords[0])
        particle2 = Dot(color=RED).move_to(particle2_coords[0])

        # Animate the trajectory
        self.add(background)
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

