# Timothy Rutkowski 03/26/24 timothyRutkowski_lab5-4.py

# This program will draw a snowman

import turtle

# Defines all constants and variables
ANIMATION_SPEED  = 0

# Variables for base
X = 0
Y_BASE = -200
RADIUS_BASE = 150

# Variables for mid section
Y_MID = 48
RADIUS_MID_SECTION = 100

# Variables for head
Y_HEAD = 198
RADIUS_HEAD = 50

# Variables for hat
  # Hat Base
X_HAT_BASE = -60
Y_HAT_BASE = 230
LINE_HAT_BASE_1 = 120
LINE_HAT_BASE_2 = 20
ANGLE_HAT = 90
  # Hat Top
X_HAT_TOP = -30 
Y_HAT_TOP = 300
LINE_HAT_TOP = 60
NUM_LINES_HAT = 4

# Variables for face
Y_EYES = 225
  # Left Eye
X_LEFT_EYE = -30
  # Right Eye
X_RIGHT_EYE = 10
RADIUS_EYES = 10
  # Mouth
X_MOUTH = -28
Y_MOUTH = 185 
ANGLE_MOUTH = 90
LINE_MOUTH = 60

# Variables for arms
  # Left Arm
X_LEFT_ARM = -100 
Y_LEFT_ARM = 50
LINE_LEFT_ARM = 80
ANGLE_LEFT_ARM = 165
ANGLE_LEFT_ELBOW = 70
  # Left Fingers
LINE_LEFT_FINGERS = 20
ANGLE_LEFT_FINGER_1 = 70
ANGLE_LEFT_FINGER_2 = 85
  # Right Arm
X_RIGHT_ARM = 100
Y_RIGHT_ARM = 50
LINE_RIGHT_ARM = 90
ANGLE_RIGHT_ARM = 50
  # Right Fingers
LINE_RIGHT_FINGERS = 20
ANGLE_RIGHT_FINGER_1 = 50
ANGLE_RIGHT_FINGER_2 = 90

# Variables for scarf
  # Scarf neck
ANGLE_SET = 10
X_SCARF = -40
Y_SCARF = 140
LINE_SCARF_1 = 80
LINE_SCARF_2 = 20
ANGLE_SCARF = 90
  # Scarf tail
X_SCARF_TAIL = 25
Y_SCARF_TAIL = 155
LINE_SCARF_TAIL_1 = 60
LINE_SCARF_TAIL_2 = 20
ANGLE_SCARF_TAIL = 15
ANGLE_SCARF_TAIL_1 = 90

# Main function of program
def main():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    draw_base()
    draw_mid_section()
    draw_head()
    draw_hat()
    draw_face()
    draw_arms()
    draw_scarf()

# Function to draw the base of the snowman    
def draw_base():
    turtle.penup()
    turtle.goto(X, Y_BASE - RADIUS_BASE)
    turtle.pendown()
    turtle.circle(RADIUS_BASE)

# Function to draw the mid section of snowman    
def draw_mid_section():
    turtle.penup()
    turtle.goto(X, Y_MID - RADIUS_MID_SECTION)
    turtle.pendown()
    turtle.circle(RADIUS_MID_SECTION) 

# Function to draw the head of the snowman    
def draw_head():
    turtle.penup()
    turtle.goto(X, Y_HEAD - RADIUS_HEAD)
    turtle.pendown()
    turtle.circle(RADIUS_HEAD)
    
# Function to draw the hat of the snowman in two parts: 
# The hat base and hat top
def draw_hat():
    # Hat base
    turtle.penup()
    turtle.goto(X_HAT_BASE, Y_HAT_BASE)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(LINE_HAT_BASE_1)
    turtle.left(ANGLE_HAT)
    turtle.forward(LINE_HAT_BASE_2)
    turtle.left(ANGLE_HAT)
    turtle.forward(LINE_HAT_BASE_1)
    turtle.left(ANGLE_HAT)
    turtle.forward(LINE_HAT_BASE_2)
    turtle.end_fill()
    # Hat top
    turtle.penup()
    turtle.goto(X_HAT_TOP, Y_HAT_TOP)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.pendown()
    for count in range (NUM_LINES_HAT):
        turtle.forward(LINE_HAT_TOP)
        turtle.left(ANGLE_HAT)
    turtle.end_fill()

# Function to draw the face of the snowman in three parts: 
# The left eye, right eye, and mouth
def draw_face():
    # Left eye
    turtle.penup()
    turtle.goto(X_LEFT_EYE, Y_EYES - RADIUS_EYES)
    turtle.pendown()
    turtle.circle(RADIUS_EYES)
    # Right eye
    turtle.penup()
    turtle.goto(X_RIGHT_EYE, Y_EYES - RADIUS_EYES)
    turtle.pendown()
    turtle.circle(RADIUS_EYES)
    # Mouth
    turtle.penup()
    turtle.goto(X_MOUTH, Y_MOUTH)
    turtle.left(ANGLE_MOUTH)
    turtle.pendown()
    turtle.forward(LINE_MOUTH)

# Function to draw the arms of the snowman in two parts: 
# The left arm with a bend in the elbow and fingers and the right arm with fingers
def draw_arms():
    # Left arm
    turtle.penup()
    turtle.goto(X_LEFT_ARM, Y_LEFT_ARM)
    turtle.left(ANGLE_LEFT_ARM)
    turtle.pendown()
    turtle.forward(LINE_LEFT_ARM)
    turtle.right(ANGLE_LEFT_ELBOW)
    turtle.forward(LINE_LEFT_ARM)
    turtle.left(ANGLE_LEFT_FINGER_1)
    turtle.forward(LINE_LEFT_FINGERS)
    turtle.penup()
    turtle.backward(LINE_LEFT_FINGERS)
    turtle.right(ANGLE_LEFT_FINGER_2)
    turtle.pendown()
    turtle.forward(LINE_LEFT_FINGERS)
    # Right arm
    turtle.penup()
    turtle.goto(X_RIGHT_ARM, Y_RIGHT_ARM)
    turtle.right(ANGLE_RIGHT_ARM)
    turtle.pendown()
    turtle.forward(LINE_RIGHT_ARM)
    turtle.left(ANGLE_RIGHT_FINGER_1)
    turtle.forward(LINE_RIGHT_FINGERS)
    turtle.penup()
    turtle.backward(LINE_RIGHT_FINGERS)
    turtle.right(ANGLE_RIGHT_FINGER_2)
    turtle.pendown()
    turtle.forward(LINE_RIGHT_FINGERS)

# Funtion to draw the scarf in two parts:
# The scarf neck and scarf tail
def draw_scarf():
    # Scarf neck
    turtle.penup()
    turtle.goto(X_SCARF, Y_SCARF)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(ANGLE_SET)
    turtle.pendown()
    turtle.forward(LINE_SCARF_1)
    turtle.left(ANGLE_SCARF)
    turtle.forward(LINE_SCARF_2)
    turtle.left(ANGLE_SCARF)
    turtle.forward(LINE_SCARF_1)
    turtle.left(ANGLE_SCARF)
    turtle.forward(LINE_SCARF_2)
    turtle.end_fill()
    # Scarf tail
    turtle.penup()
    turtle.goto(X_SCARF_TAIL, Y_SCARF_TAIL)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(ANGLE_SCARF_TAIL)
    turtle.forward(LINE_SCARF_TAIL_1)
    turtle.left(ANGLE_SCARF_TAIL_1)
    turtle.forward(LINE_SCARF_TAIL_2)
    turtle.left(ANGLE_SCARF_TAIL_1)
    turtle.forward(LINE_SCARF_TAIL_1)
    turtle.left(ANGLE_SCARF_TAIL_1)
    turtle.forward(LINE_SCARF_TAIL_2)
    turtle.end_fill()
    
main()
turtle.done()