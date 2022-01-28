# 2.4.2 TempConvert.py

TempStr = input("Please type in the temperature with symbol:")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("The converted temperature is{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("The converted temperature is{:.2f}F".format(F))
else:
    print("Wrong format.")