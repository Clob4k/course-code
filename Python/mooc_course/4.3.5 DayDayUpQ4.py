# 4.3.5 DayDayUpQ4.py

def DayUp(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup

dayfactor = 0.01
while DayUp(dayfactor) < 37.78:
    dayfactor += 0.0001
print("factor:{:.3f}".format(dayfactor))