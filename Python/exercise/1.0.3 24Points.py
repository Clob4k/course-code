# 1.0.3 24Points.py
from itertools import permutations

def main(Num1, Num2, Num3, Num4):
    print("-------------------")
    Cal3(Num1, Num2, Num3, Num4)
    Cal2(Num1, Num2, Num3, Num4)
    Cal1(Num1, Num2, Num3, Num4)
    print("-------------------")

def Cal3(Num1, Num2, Num3, Num4):
    trial1 = Num1 + Num2 + Num3 + Num4
    trial2 = Num1 * Num2 * Num3 * Num4
    if trial1 == 24:
        print(Num1,'+',Num2,'+',Num3,'+',Num4,'= 24')
    if trial2 == 24:
        print(Num1,'*',Num2,'*',Num3,'*',Num4,'= 24')

def Cal2(Num1, Num2, Num3, Num4):
    sym = ['+','-','*','/']
    num = [Num1, Num2, Num3, Num4]
    plist = list(permutations(sym,3))
    nlist = list(permutations(num,4))
    for i in range(len(nlist)):
        ntuple = nlist[i]
        num1, num2, num3, num4 = ntuple
        for i in range(len(plist)):
            ptuple = plist[i]
            fir, sec, thr = tuple(ptuple)
            cal = str(num1)+" "+fir+" "+str(num2)+" "+sec+" "+str(num3)+" "+thr+" "+str(num4)
            res = eval(cal)
            if res == 24.0:
                print(cal,"= 24")

def Cal1(Num1, Num2, Num3, Num4):
    sym = ['+','-','*','/']
    num = [Num1, Num2, Num3, Num4]
    plist = list(permutations(sym,2))
    nlist = list(permutations(num,4))
    for i in range(len(nlist)):
        ntuple = nlist[i]
        num1, num2, num3, num4 = ntuple
        for i in range(len(plist)):
            ptuple = plist[i]
            fir, sec = tuple(ptuple)
            cal1 = str(num1)+" "+fir+" "+str(num2)+" "+fir+" "+str(num3)+" "+sec+" "+str(num4)
            res1 = eval(cal1)
            cal2 = str(num1)+" "+fir+" "+str(num2)+" "+sec+" "+str(num3)+" "+fir+" "+str(num4)
            res2 = eval(cal2)
            cal3 = str(num1)+" "+sec+" "+str(num2)+" "+fir+" "+str(num3)+" "+fir+" "+str(num4)
            res3 = eval(cal3)
            if res1 == 24:
                print(cal1,"= 24")
            elif res2 == 24:
                print(cal2,"= 24")
            elif res3 == 24:
                print(cal3,"= 24")

try:
    Num1 = input()
    Num2 = input()
    Num3 = input()
    Num4 = input()
    if len(Num1) and len(Num2) and len(Num3) and len(Num4) > 1:
        print("invaild input")
    else:
        main(eval(Num1), eval(Num2), eval(Num3), eval(Num4))
except:
    print("invaild input")