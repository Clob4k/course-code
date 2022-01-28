# 5.2.6 ErrorDispose.py

try:
    num = input("please type in a integer:")
    cnNum = "零一二三四五六七八九"
    for i in num:
        print(cnNum[eval(i)], end ='')
except NameError:
    print("Non-integer input.")