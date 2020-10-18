import turtle
import keyboard

# variables
snake_segments = []
x = 0
boxes =    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
move_direction = 0
box = 4
box_xcor = [0, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
box_ycor = [0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 175, 175, 175, 175, 175, 175, 175, 175, 175, 175, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, -25, -25, -25, -25, -25, -25, -25, -25, -25, -25, -75, -75, -75, -75, -75, -75, -75, -75, -75, -75, -125, -125, -125, -125, -125, -125, -125, -125, -125, -125, -175, -175, -175, -175, -175, -175, -175, -175, -175, -175, -225, -225, -225, -225, -225, -225, -225, -225, -225, -225]
print(len(box_ycor))

# screen setup
wn = turtle.Screen()
wn.title("Snake Alpha")
wn.setup(width = 600, height = 600)
wn.tracer(0)

# turtle setup
grid = turtle.Turtle()
grid.penup()
grid.hideturtle()

# functions
# grid
def draw_grid():
    # local variables
    xcor = -250
    ycor = 250

    # turtle direction
    grid.setheading(270)

    # line drawing
    for x in range(0, 11):
        grid.goto(xcor, 250)
        grid.pendown()
        grid.forward(500)
        grid.penup()
        xcor += 50

    grid.setheading(0)
    for x in range(0, 11):
        grid.goto(-250, ycor)
        grid.pendown()
        grid.forward(500)
        grid.penup()
        ycor -= 50

# adds new segment to the snake
def snake_size_plus1():
    # global variables
    global snake_segments
    global x
    x = len(snake_segments) + 1
    # main code
    snake_segments.append(str(x))
    snake_segments[x - 1] = turtle.Turtle()
    snake_segments[x - 1].speed(0)
    snake_segments[x - 1].shape("square")
    snake_segments[x - 1].color("blue")
    snake_segments[x - 1].shapesize(stretch_len = 2.5, stretch_wid = 2.5)
    snake_segments[x - 1].penup()

# sets direction for snake
def snake_left():
    global move_mechanism
    move_mechanism = "left"
    snake_box()

# sets direction for snake
def snake_right():
    global move_direction
    move_direction = "right"
    snake_box()

# sets direction for snake
def snake_up():
    global move_direction
    move_direction = "up"
    snake_box()

# sets direction for snake
def snake_down():
    global move_direction
    move_direction = "down"
    snake_box()

# decides what box the snake should go in
def snake_box():
    global move_direction
    global box
    dummy = box

    if move_direction == "left":
        pass

    elif move_direction == "right":
        pass

    elif move_direction == "up":
        box += 10
        if box > 0:
            move_snake()
        else:
            box = dummy

    elif move_direction == "down":
        pass
# move snake
def move_snake():
    global box
    global box_xcor
    global box_ycor
    global snake_segments
    snake_segments[0].goto(box_xcor[box], box_ycor[box])
    
# drawing grid
draw_grid()
# creating snake
snake_size_plus1()
snake_segments[0].goto(-25, 25)

while True:
    # upgrading manually
    wn.update()
    # snake up
    if keyboard.is_pressed("up"):
        snake_up()
        print(box)

turtle.done()