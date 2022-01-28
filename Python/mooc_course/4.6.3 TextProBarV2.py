# 4.6.3 TextProBarV1.py
import time

for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.05)