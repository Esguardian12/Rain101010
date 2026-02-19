from turtle import *
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(50)
screen._root.attributes('-alpha', 0.8)
hideturtle()

chars = '01' * 1000
num_columns = 500
turtles = []
font = ('Courier', 14, 'normal')

for i in range(num_columns):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.color('green')
    x = -380 + i * 5
    y = random.randint(-300, 300)
    t.goto(x, y)
    turtles.append(t)

def move_rain():

    char = random.choice(chars)
    t.write(char , align = 'center', font=font)

    y = t.ycor() - 20
    if y < -300:
        y = 300
        t.goto(t.xcor() + random.randint(-5, 5), y)
        t.color(random.choice(['green', 'lime green', 'forest green']))

    update()
    ontimer(move_rain, 80)

move_rain()
done()
