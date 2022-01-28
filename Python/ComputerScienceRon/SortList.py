# BubbleSort.py
from random import randint

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

def insertionSort(List):
    for pointer in range(1, len(List)-1):
        ItemToBeInserted = List[pointer]
        CurrentItem = pointer - 1
        while List[CurrentItem] > ItemToBeInserted and CurrentItem > -1:
            List[CurrentItem+1] = List[CurrentItem]
            CurrentItem = CurrentItem - 1
        List[CurrentItem+1] = ItemToBeInserted
    return List

def binarySearch(List, SearchItem):
    Found = False
    SearchFailed = False
    First = 0
    Last = len(List) - 1
    while not Found and not SearchFailed:
        Middle = (First+Last) // 2
        if List[Middle] == SearchItem:
            Found = True
        else:
            if First >= Last:
                SearchFailed = True
            else:
                if List[Middle] > SearchItem:
                    Last = Middle - 1
                else:
                    First = Middle + 1
    if Found == True:
        print("The Index for item {} is {}".format(SearchItem, Middle))
    else:
        print("Item not found")

def randomList():
    global List
    elements = int(input("Number Of Elements:"))
    for i in range(elements):
        List.append(randint(1,1000))
    print("List updated:", List)    

def keyInList():
    global List
    Add = input("Add a Element(press enter to end):")
    while Add != "":
        List.append(int(Add))
        print("List updated:", List)
        Add = input("Add a element(press enter to end):")

def main():
    global List
    print('''
0.Reset List(clear)\n
1.Current List\n
2.Generate Random List(append)\n
3.Key In List(append)\n
4.Bubble Sort\n 
5.Insertion Sort\n
6.Binary Search(sequencial order)\n
press enter to exit
''')
    Case = input()
    while Case != "":
        Case = int(Case)
        if Case == 0:
            List = []
        elif Case == 1:
            print(List)
        elif Case == 2:
            randomList()
        elif Case == 3:
            keyInList()
        elif Case == 4:
            bubbleSort(List)
            print("List updated:", List)
        elif Case == 5:
            insertionSort(List)
            print("List updated:", List)
        elif Case == 6:
            Item = int(input("Key in item to search(integer):"))
            bubbleSort(List)
            binarySearch(List, Item)
        Case = input()
    exit()

List = []
main()
