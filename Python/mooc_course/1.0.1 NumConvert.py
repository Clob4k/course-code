# 1.0.1 NumConvert.py

cnNum = "零一二三四五六七八九"
num = input("please enter a number.")
for i in num:
    print(cnNum[eval(i)], end ='')