# 1.2 binary search.py

def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

test_list = [1, 3, 5, 7, 9]
# element "3" (exist) 
print("element index:", binary_search(test_list,3))
# element "-1" (not exist) 
print("element index:", binary_search(test_list,-1))