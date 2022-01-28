# 4.5.4 TimeFormat.py
import time

t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))