# 1.0.6 MathExpansion.py
import math

def Tier1(a,x,n):
    repet = int(input("repet="))
    for i in range (repet):
        frc = Fract(i+1,n)
        buf = pow(a,n) * (frc) / math.factorial(i) * pow((x/a),i)
        print(buf)

def Fract(i,n):
    if i >= 2:
        while i >= 2:
            sum = n * (n-1)
            i = i-1
        return sum
    else:
        return 1
        
    
def main():
    option = input("")
    if option == '1':
        x = float(input("x="))
        n = float(input("n="))
        a = float(input("a="))
        Tier1(a,x,n)
    elif option == 2:
        x = input("x=")
        n = input("n=")
    else:
        print("invalid number")

main()

