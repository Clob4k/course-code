# 1.0.5 MotionGraphing.py
import turtle

def DrawOpt():
    opt = input('''''')
    if opt == 1:
        DrawUp()
    else:
        print('')

def DrawUp():
    length = input()
    turtle.setup()
    turtle.penup()
    turtle.seth(0)
    while True:
        turtle.pendown()
        turtle.penup()
        turtle.fd(length)