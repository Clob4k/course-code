# 1.0.2 DayDayUp.py

def DayUp(dayfactor):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup = dayup*(1 - dayfactor)
        else:
            dayup = dayup*(1 + dayfactor)
    print("Progress:{:.2f}".format(dayup))
    return dayup

while 1:    
    dayfactor = eval(input("Entering the dayup factor"))
    DayUp(dayfactor)