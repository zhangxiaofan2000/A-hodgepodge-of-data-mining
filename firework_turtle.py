# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/13 9:35
# File : firework_tutle.py

def firework1():
    import turtle
    import random

    # Set the window size
    turtle.setup(800, 600)

    # Create a turtle object
    t = turtle.Turtle()

    # Set the turtle's speed to the maximum
    t.speed(0)

    # Set the background color to black
    turtle.bgcolor('black')

    # Define a function to create a firework
    def firework(x, y):
      # Move the turtle to the starting position
      t.penup()
      t.goto(x, y)
      t.pendown()

      # Choose a random color for the firework
      t.color(random.random(), random.random(), random.random())

      # Draw the firework
      for i in range(20):
        t.forward(20)
        t.backward(20)
        t.right(36)

    # Create a firework at the starting position
    firework(0, 0)

    # Create a firework at a random position
    firework(random.randint(-200, 200), random.randint(-200, 200))

    # Create a firework at a random position
    firework(random.randint(-200, 200), random.randint(-200, 200))

    # Create a firework at a random position
    firework(random.randint(-200, 200), random.randint(-200, 200))

    # Keep the window open until it is clicked
    turtle.mainloop()

import turtle
def firework2():
    # Set the background color
    turtle.bgcolor("black")

    # Create a turtle object
    firework = turtle.Turtle()

    # Set the turtle shape, color, and speed
    firework.shape("circle")
    firework.color("red")
    firework.speed(0)

    # Move the turtle to the starting position
    firework.penup()
    firework.goto(0, 200)
    firework.pendown()

    # Create a loop to draw the fireworks
    for i in range(20):
      # Draw the explosion
      firework.color("orange")
      firework.circle(10 * i)

      # Move the turtle up and to the right
      firework.penup()
      firework.forward(10)
      firework.right(20)
      firework.pendown()

      # Draw the sparks
      firework.color("yellow")
      firework.circle(10 * i)

    # Hide the turtle
    firework.hideturtle()
