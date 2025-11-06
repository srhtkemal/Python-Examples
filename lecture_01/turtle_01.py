import turtle 
from random import random
turtle.bgcolor("orange")

t = turtle.Turtle()

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()