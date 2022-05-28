# 2.2 insertion sort.py

def insertionSort(List):
    for pointer in range(1, len(List)-1):
        ItemToBeInserted = List[pointer]
        CurrentItem = pointer - 1
        while List[CurrentItem] > ItemToBeInserted and CurrentItem > -1:
            List[CurrentItem+1] = List[CurrentItem]
            CurrentItem = CurrentItem - 1
        List[CurrentItem+1] = ItemToBeInserted
    return List

print(insertionSort([5, 3, 1, 2, 6]))