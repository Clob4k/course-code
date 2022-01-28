# 1.0.2 CollatzConjecture.py

Num = eval(input())
while Num != 1:
    if Num % 2 == 0:
        Num = Num / 2
    else:
        Num = Num * 3 + 1
    print(Num)
