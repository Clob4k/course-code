# 1.0.7 MutiTable.py

Num = eval(input())
for row in range(Num):
    for line in range(Num):
        print((row + 1) * (line + 1), end="")
    print("")