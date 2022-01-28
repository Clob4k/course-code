# 6.4.5 HanoiTower.py

count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1, mid, dst, src)

try:
    a = eval(input("plaese enter a number."))
    hanoi(a, "A", "C", "B")
    print(count)
except:
    print("wrong format.")