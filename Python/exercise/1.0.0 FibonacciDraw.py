# 1.0.3 FibonacciDraw.py
import math
import turtle

def fiboseq(n):
    for i in range(n):
        seq = (1/math.sqrt(5)) * (((1+math.sqrt(5)) / 2)**(i+2) - ((1-math.sqrt(5))/2)**(i+2))
        seqint = round(seq, 1)
        fibocir(seqint)

def fibocir(a):
    turtle.circle(a, 90)

def main():
    level = eval(input("Enter the level for the sqare."))
    turtle.pendown()
    turtle.pensize(2)
    turtle.seth(180)
    fiboseq(level)

main()