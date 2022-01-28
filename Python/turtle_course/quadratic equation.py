import math

while 1:

    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))

    delta = b*b-4*a*c

    if delta > 0:
        x1 = float(-b + math.sqrt(delta)) / (2*a)
        x2 = float(-b - math.sqrt(delta)) / (2*a)
        print('x1=',x1,'x2=',x2)
    else:
        if delta == 0:
            x1 = x2 = (-b) / (2*a)
            print('x1 = x2 = ', x1)
        else:
            print("none real root!")