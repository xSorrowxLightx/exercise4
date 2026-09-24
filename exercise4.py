import turtle

#All of the exercises are in this program :U

def draw_square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def draw_rectangle(t, length, width):
    for i in range(4):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)

def jump(length):
    """Move forward without leaving a trail
    Post condition: leaves the pen down."""
    t.penup()
    t.forward(length)
    t.pendown()

def draw_rhombus(t, length):
    for i in range(2):
        t.forward(length)
        t.left(60)
        t.forward(length)
        t.left(120)

#---------

t = turtle.Turtle()

t.speed(10)
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("blue")

screen.setup(width=600, height=600)

t.clear()

#---------

draw_square(t, 100)
jump(-200)
draw_square(t, 100)

draw_rectangle(t, 100, -200)

draw_rhombus(t, 50)

#^^^This also counts as a parellelogram so im counting it as gud

#---------

turtle.exitonclick()
