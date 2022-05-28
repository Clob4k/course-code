# 1.1 bubble sort.py

def bubbleSort(List):
    n = len(List) - 1
    NoMoreSwaps = False
    while NoMoreSwaps == False:
        NoMoreSwaps = True
        for i in range(n):
            if List[i] > List[i+1]:
                Temp = List[i]
                List[i] = List[i+1]
                List[i+1] = Temp
                NoMoreSwaps = False
        n -= 1
    return List

print(bubbleSort([5, 3, 1, 2, 6]))