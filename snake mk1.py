# snake mk1.1
# developed by Blip Blop Inc. 2020*
# import libraries
import turtle
import keyboard
import time
import random

# variables
# x coordinates of the box
box_xcor = [0, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
# y coordinates of the box
box_ycor = [0, 225, 175, 125, 75, 25, -25, -75, -125, -175, -225]
x_index = 5
y_index = 5
x_snack_index = None
y_snack_index = None
direction = 90
game_tick = 0.175
snake_died = False
snack_eaten = True
snake_length = 1
snack_delay = 1
snack_delay_counter = 0
box_xcor_past = [5]
box_ycor_past = [5]
snake_segments = ["s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10",
                  "s11", "s12", "s13", "s14", "s15", "s16", "s17", "s18", "s19", "s20",
                  "s21", "s22", "s23", "s24", "s25", "s26", "s27", "s28", "s29", "s30",
                  "s31", "s32", "s33", "s34", "s35", "s36", "s37", "s38", "s39", "s40",
                  "s41", "s42", "s43", "s44", "s45", "s46", "s47", "s48", "s49", "s50",
                  "s51", "s52", "s53", "s54", "s55", "s56", "s57", "s58", "s59", "s60",
                  "s61", "s62", "s63", "s64", "s65", "s66", "s67", "s68", "s69", "s70",
                  "s71", "s72", "s73", "s74", "s75", "s76", "s77", "s78", "s79", "s80",
                  "s81", "s82", "s83", "s84", "s85", "s86", "s87", "s88", "s89", "s90",
                  "s91", "s92", "s93", "s94", "s95", "s96", "s97", "s98", "s99", "s100"]
snake_length_old = 1

# setup
# turtle window setup
wn = turtle.Screen()
wn.title("Snake mk1.1")
wn.bgcolor("white")
wn.setup(width = 700, height = 700)
wn.tracer(0)

# auxiliary turtle setup
aux_turtle = turtle.Turtle()
aux_turtle.hideturtle()
aux_turtle.penup()

# first snake segment setup
s1 = turtle.Turtle()
s1.shape("square")
s1.color("green")
s1.shapesize(stretch_len = 2.5, stretch_wid = 2.5)
s1.penup()
s1.goto(box_xcor[x_index], box_ycor[y_index])

# snack setup
snack = turtle.Turtle()
snack.shape("square")
snack.color("red")
snack.shapesize(stretch_len = 2.5, stretch_wid = 2.5)
snack.penup()
snack.hideturtle()

# functions
# setup functions
# draw grid
def draw_grid():
    aux_turtle.goto(-250, 250)
    aux_turtle.setheading(270)
    # draws horizontal lines
    for x in range(0, 11):
        aux_turtle.pendown()
        aux_turtle.sety(-250)
        aux_turtle.penup()
        aux_turtle.goto(aux_turtle.xcor() + 50, 250)
    aux_turtle.goto(-250, 250)
    aux_turtle.setheading(0)
    # draws vertical lines
    for x in range(0, 11):
        aux_turtle.pendown()
        aux_turtle.setx(250)
        aux_turtle.penup()
        aux_turtle.goto(-250, aux_turtle.ycor() - 50)

# game loop function
# snake direction
def set_snake_direction():
    # variables
    global direction
    # directions are turtle use same numbering system as turtle set heading
    # left key pressed, set snake direction left
    if keyboard.is_pressed("left") and direction != 0:
        direction = 180
    # right key pressed, set snake direction right
    elif keyboard.is_pressed("right") and direction != 180:
        direction = 0
    # up key pressed, set snake direction up
    elif keyboard.is_pressed("up") and direction != 270:
        direction = 90
    # down key pressed, set snake direction down
    elif keyboard.is_pressed("down") and direction != 90:
        direction = 270

# move snake
def move_snake():
    # variables
    global box_xcor
    global box_ycor
    global x_index
    global y_index
    global direction
    global snake_died
    # move left
    if direction == 180:
        x_index = x_index - 1
    # move right
    elif direction == 0:
        x_index = x_index + 1
    # move up
    elif direction == 90:
        y_index = y_index - 1
    # move up
    elif direction == 270:
        y_index = y_index + 1

    box_xcor_past.append(x_index)
    box_ycor_past.append(y_index)

    # snake hit wall?
    if x_index < 1 or x_index > 10 or y_index < 1 or y_index > 10:
        print("snake died")
        print("snake crashed in wall")
        snake_died = True
    else:
        s1.setx(box_xcor[x_index])
        s1.sety(box_ycor[y_index])

# move snack
def move_snack():
    # variables
    global box_xcor
    global box_ycor
    global x_snack_index
    global y_snack_index
    global snack_eaten
    # main code
    # checks if snack is all ready on the grid
    if snack_eaten == True:
        # rng snack generation
        x_snack_index = random.randint(1, 10)
        y_snack_index = random.randint(1, 10)
        snack.goto(box_xcor[x_snack_index], box_ycor[y_snack_index])
        snack.showturtle()
        snack_eaten = False

# eat snack
def eat_snack():
    # variables
    global box_xcor
    global box_ycor
    global x_index
    global y_index
    global x_snack_index
    global y_snack_index
    global snack_eaten
    global snake_length
    # main loop
    # checks if snack has been eaten
    if snack_eaten == False:
        # checks if snake is eating the snack
        if x_index == x_snack_index and y_index == y_snack_index:
            snack_eaten = True
            snake_length = snake_length + 1
            snack.hideturtle()
        else:
            for x in range(0, snake_length - 1):
                pass

# delay snack
def delay_snack():
    # variable
    global snack_delay
    global snack_delay_counter
    # sets the delay
    snack_delay = random.randint(5, 25)
    snack_delay_counter = 0

# grow snake
def grow_snake():
    # variable
    global snake_length
    global snake_segments
    global snake_length_old
    # main code
    if snake_length != snake_length_old:
        snake_length_old = snake_length
        snake_segments[snake_length - 2] = turtle.Turtle()
        snake_segments[snake_length - 2].shape("square")
        snake_segments[snake_length - 2].color("blue")
        snake_segments[snake_length - 2].shapesize(stretch_len=2.5, stretch_wid=2.5)
        snake_segments[snake_length - 2].penup()

# control other snake segments
def tail_control():
    # variables
    global snake_length
    global snake_segments
    global box_xcor_past
    global box_ycor_past
    global box_xcor
    global box_ycor
    global snake_died
    x = None
    y = None
    n = None

    # main code
    if snake_died == False:
        if snake_length >= 2:
            for j in range(0, snake_length - 1):
                n = j + 2
                n = n * -1
                x = box_xcor[box_xcor_past[n]]
                y = box_ycor[box_ycor_past[n]]
                snake_segments[j].goto(x, y)

# snake encircled
def snake_encircled():
    # variables
    global snake_length
    global snake_segments
    global snake_died
    # main code
    for x in range(0, snake_length - 1):
        if s1.xcor() == snake_segments[x].xcor() and s1.ycor() == snake_segments[x].ycor():
            snake_died = True
            print("snake died")
            print("snake encircled")
            break

# execute setup functions
draw_grid()
delay_snack()
wn.update()
time.sleep(2)

# main game loop
while True:
    # breaks while true if the snake died
    if snake_died == True:
        break
    # checks to see if the user is changing the direction of the snake
    set_snake_direction()
    # moves the snake in the direction told
    snake_encircled()
    move_snake()
    # the game starts when the user presses any input in the keyboard.
    # in order for the snack to generate properly with the random delays this loop is necessary
    if direction != None:
        snack_delay_counter = snack_delay_counter + 1
        if snack_delay == snack_delay_counter:
            move_snack()
            delay_snack()

    eat_snack()
    grow_snake()
    tail_control()
    time.sleep(game_tick)
    wn.update()

# end turtle
turtle.done()