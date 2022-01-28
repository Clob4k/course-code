# StuMarkArray.py

def InputName():
    Temp = input("Enter the Student Name(press enter to exit):")
    Count = StuList.count
    while Temp != "":
        StuList[Count+1] = Temp
    print("Exit Name input")

def InputMark():
    Temp = input("Enter the student Mark(press enter to exit):")
    Count = StuMark.count
    while Temp != "":
        StuMark[Count+1] = Temp
    print("Exit Mark input")

StuList = []
StuMark = []
InputName()
