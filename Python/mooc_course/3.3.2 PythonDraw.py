# 3.3.2 PythonDraw.py

import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup() #turtle.pu()
turtle.fd(-250) #turtle.forward(-250)
turtle.pendown() #turtle.pd()
turtle.pensize(25) #turtle.width(25)
turtle.pencolor("purple") #turtle.pencolor(0.63, 0.13, 0.94)
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()