# 4.2 quick sort.py

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([6, 5, 2, 9, 8, 7, 4, 1]))

'''
dry-run

[6, 5, 2, 9, 8, 7, 4, 1]

[5, 2, 4, 1] [6] [9, 8, 7]

[2, 4, 1] [5] [6] [8, 7] [9]

[1] [2] [4] [5] [6] [7] [8] [9]

'''