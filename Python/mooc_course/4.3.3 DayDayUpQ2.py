# 4.3.3 DayDayUpQ2.py

dayfactor = 0.005
dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)

print("progress:{:.2f}, retrogress:{:.2f}" .format(dayup, daydown))