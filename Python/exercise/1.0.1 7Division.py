# 1.0.4 7Division.py
from time import perf_counter

def layer1(n):
    global count
    for i in range(10, 99):
        add = i
        for i in range(10, 99):
            quo = add*1000 + 700 + i
            trail1 = n * quo
            count = count + 1
            # print("\rattempts:{}".format(count), end="") 
            if str(trail1)[-8] in ['7']  and len(str(trail1)) == 10:
                layer2(trail1, quo, n)

def layer2(dividend, quotient, divisor):
    trail2 = dividend - eval(str(quotient)[0]) * divisor * 10000
    if str(trail2)[-5] in ['7'] and len(str(trail2)) == 10:
        layer3(dividend, quotient, divisor, trail2) 

def layer3(dividend, quotient, divisor, trail2):
    trail3 = trail2 - eval(str(quotient)[1]) * divisor * 1000
    trail4 = 700 * divisor
    if len(str(trail3)) == 8 :
        if str(trail3)[-7] in ['7'] and str(trail4)[-7] in ['7']:
            trail5 = trail3 - trail4
            layer4(dividend, quotient, divisor, trail5, trail4, trail3, trail2)

def layer4(dividend, quotient, divisor, trail5, trail4, trail3, trail2):
    trail6 = eval(str(quotient)[3]) * divisor * 10
    trail7 = trail5 - trail6
    trail8 = eval(str(quotient)[4]) * divisor
    if len(str(trail6)) == 8 and len(str(trail7)) == 6 and len(str(trail8)) == 6:
        if str(trail6)[-4] in ['7'] and trail7 == trail8:
            print("\nSolution: dividend:{},quotient:{},divisor:{}".format(dividend, quotient, divisor))
            trail9 = eval(str(quotient)[0]) * divisor * 10000
            trail10 = eval(str(quotient)[1]) * divisor * 1000
            PrintFom(dividend,trail9,trail2,trail10,trail3,trail4,trail5,trail6,trail7,trail8,divisor,quotient)
            
def PrintFom(dividend,trail9,trail2,trail10,trail3,trail4,trail5,trail6,trail7,trail8,divisor,quotient):
    print(''' 
                     {11}  
            ----------------
    {10} /    {0}
                {1}
            ----------------
                {2}
                {3}
            ----------------
                  {4}
                  {5}
            ----------------
                  {6}
                  {7}
            ----------------
                    {8}
                    {9}
            ----------------
                         0
            
            '''.format(dividend,trail9,trail2,trail10,trail3,trail4,trail5,trail6,trail7,trail8,divisor,quotient))

def main():
    start = perf_counter()
    for i in range(1000, 1999):
        pl = i
        for i in range(1, 10):
            div = 70 + pl*100 + i
            layer1(div)
    print("attempts:{}".format(count))
    print("operation time:{:.2f}s".format(perf_counter()-start))

count = 0   
main()