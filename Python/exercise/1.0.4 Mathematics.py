# 1.0.4 Mathematics.py
import math

def sinplus(a,b):
    global R, α, deg
    CalabR(a,b)
    print("{}sin(θ+{:.2f})".format(R,α))
    print("{}sin(θ+{:.2f})".format(R,deg))

def sinmin(a,b):
    global R, α, deg
    CalabR(a,b)
    print("{}sin(θ-{:.2f})".format(R,α))
    print("{}sin(θ-{:.2f})".format(R,deg))

def cosplus(a,b):
    global R, α, deg
    CalabR(a,b)
    print("{}sin(θ-{:.2f})".format(R,α))
    print("{}sin(θ-{:.2f})".format(R,deg))

def cosmin(a,b):
    global R, α, deg
    CalabR(a,b)
    print("{}sin(θ+{:.2f})".format(R,α))
    print("{}sin(θ+{:.2f})".format(R,deg))


def CalabR(a,b):
    global R, α, deg
    aR = math.sqrt(a**2 + b**2)
    if isinstance(aR,int):
        R = aR
    else:
        bR = a**2 + b**2
        R = '√'+str(bR)

    α = math.atan(b/a)
    deg = math.degrees(α)

def Ran():
    Inran = input("Please enter the max range(eg. 180, 360).")
    Ouran = math.radians(eval(Inran))
    return Ouran

def LeftHS(L):
    global LHS
    Le = str(L)
    Le = Le.upper()
    Le = Le.replace('COSEC(@)','(1/math.sin(i))')
    Le = Le.replace('SEC(@)','1/math.cos(i)')
    Le = Le.replace('COT(@)','1/math.tan(i)')
    Le = Le.replace('SIN(2@)','2*math.sin(i)*math.cos(i)')
    Le = Le.replace('COS(2@)','(2*(math.cos(i))**2-1)')
    Le = Le.replace('TAN(2@)','(2*tan(i))/(1-(tan(i)**2))')
    Le = Le.replace('SIN(','math.sin(')
    Le = Le.replace('COS(','math.cos(')
    Le = Le.replace('TAN(','math.tan(')
    Le = Le.replace('@','i')
    Le = Le.replace('D(','math.radians(')
    LHS = Le

def RihgtHS(R):
    global RHS
    Re = str(R)
    Re = Re.upper()
    Re = Re.replace('COSEC(@)','(1/math.sin(i))')
    Re = Re.replace('SEC(@)','1/math.cos(i)')
    Re = Re.replace('COT(@)','1/math.tan(i)')
    Re = Re.replace('SIN(2@)','2*math.sin(i)*math.cos(i)')
    Re = Re.replace('COS(2@)','(2*(math.cos(i))**2-1)')
    Re = Re.replace('TAN(2@)','(2*tan(i))/(1-(tan(i)**2))')
    Re = Re.replace('SIN(','math.sin(')
    Re = Re.replace('COS(','math.cos(')
    Re = Re.replace('TAN(','math.tan(')
    Re = Re.replace('@','i')
    Re = Re.replace('D(','math.radians(')
    RHS = Re

def SolvE(LHS, RHS):
    print(LHS,"=",RHS)
    i = 0
    rad = []
    de = []
    while i <= range:
        try:
            R = eval(RHS)
            L = eval(LHS)
            if round(R,5) == round(L,5):
                rad.append(round(i,3))
                i = i+0.000002
            else:
                i = i+0.000002
        except:
            i = i+0.000002
    rad = set(rad)
    for i in rad:
        de.append(round(math.degrees(i),1))
    de = set(de)
    print(rad)
    print(de)

def Quad():
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
            print("no REAL root!")

def getNum():
    nums = []
    iNumStr = input("Please enter a number.")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("Please enter a number.")
    return nums

def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

def main():
    global range
    Option = eval(input('''--------------------
1:asinθ+bsinθ=c
2:trigonometry equations
3:quadratic equations
4:stat:main/dev/median
--------------------\n'''))

    if Option == 1:
        inputabR = eval(input
        ('''----------
1: sin+cos
2: sin-cos
3: cos+sin
4: cos-sin
----------\n'''))
        a = eval(input("a="))
        b = eval(input("b="))
        if inputabR == 1:
            sinplus(a,b)
        elif inputabR == 2:
            sinmin(a,b)
        elif inputabR == 3:
            cosplus(a,b)
        elif inputabR == 4:
            cosmin(a,b)
        else:
            print("invalid input")

    elif Option == 2:
        print('''--------------------------------------------------
common: sin(@) cos(@) tan(@) cosec(@) sec(@) cot(@)
compound angle: sin(2@) cos(2@) tan(2@)
double angle: sin(@+d(30)) Use d() when expressing degrees
--------------------------------------------------''')
        range = Ran()
        L = input("LHS:")
        R = input("RHS:")
        LeftHS(L)
        RihgtHS(R)
        SolvE(LHS, RHS)

    elif Option == 3:
        print("----------")
        Quad()

    elif Option == 4:
        n = getNum()
        m = mean(n)
        d = dev(n, m)
        med = median(n)
        print("Average:{:.2f}, Deviation:{:.2f}, Median:{:.2f}.".format(m,d,med))
    else:
        print("wrong format")

R, α, LHS, RHS = "","","",""
deg = 0
range = math.pi
while True:
    main()
