#Tkinter.py
from random import randint
import tkinter as tk
import tkinter.messagebox

def freshDisplayList():
    textList.set("CurrentList:\n"+str(List))

def randomList():
    global List, displayText, currentProgram
    displayText.set("RANDOMLIST: Input Number Of Elements:")
    currentProgram = "ranlist"

def genRanList(elements):
    global List
    for i in range(elements):
        List.append(randint(1,100))
    freshDisplayList()

def clickSubmit(event):
    elements = entryText()
    if elements != False:
        if currentProgram == "ranlist":
            genRanList(int(elements))
        elif currentProgram == "keyinlist":
            addList(int(elements))
        elif currentProgram == "binarysearch":
            binarySearch(int(elements))

def entryText():
    var = entry.get()
    if var != "":
        return var
    else:
        return False

def keyInList():
    global List, currentProgram
    displayText.set("KEYINLIST: Add a Element:")
    currentProgram = "keyinlist"

def addList(element):
    global List
    List.append(element)
    freshDisplayList()

def bubbleSort():
    global List
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
    freshDisplayList()

def insertionSort():
    global List
    for pointer in range(1, len(List)-1):
        ItemToBeInserted = List[pointer]
        CurrentItem = pointer - 1
        while List[CurrentItem] > ItemToBeInserted and CurrentItem > -1:
            List[CurrentItem+1] = List[CurrentItem]
            CurrentItem = CurrentItem - 1
        List[CurrentItem+1] = ItemToBeInserted
    freshDisplayList()

def itemSearch():
    global currentProgram
    displayText.set("BINARYSEARCH: Key In a Element:")
    currentProgram = "binarysearch"

def binarySearch(SearchItem):
    global List
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
        tkinter.messagebox.showinfo(title='ItemFound', message="The Index for item "+ str(SearchItem)+" is "+str(Middle))
    else:
        tkinter.messagebox.showinfo(title='ItemNotFound', message='Item ' + str(SearchItem) + ' does no present in the list')
    freshDisplayList()

def outputFile():
    exit()

def readFile():
    exit()    

def clearList():
    global List
    List = []
    freshDisplayList()

List = []
currentProgram = "none"

#guiStart
window = tk.Tk()
window.title("PythonList")
window.geometry('400x200')

#menubar
menubar = tk.Menu(window)

inOutPut = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=inOutPut)
inOutPut.add_command(label="read from file")
inOutPut.add_command(label="output as file")

general = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="List", menu=general)
general.add_command(label="clear list", command=clearList)
general.add_command(label="random list", command=randomList)
general.add_command(label="key in list", command=keyInList)

sorting = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Sort", menu=sorting)
sorting.add_command(label="bubble sort", command=bubbleSort)
sorting.add_command(label="insertion sort", command=insertionSort)

search = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Search", menu=search)
search.add_command(label="binary search",command=itemSearch)

window.config(menu=menubar)

#current list display
textList = tk.StringVar()
window.update()
CurrentList = tk.Label(window, textvariable=textList, wraplength=(window.winfo_width()-50))
CurrentList.pack()
freshDisplayList()

#instruction display
displayText = tk.StringVar()
displayText.set("Choose a function from MENU")
CurrentText = tk.Label(window, textvariable=displayText)
CurrentText.pack()

#entryBox
entry = tk.Entry(window)
entry.pack()

#submitButton
submit = tk.Button(window, text="submit")
window.bind('<Return>', clickSubmit)
submit.bind('<Button-1>', clickSubmit)
submit.pack()

window.mainloop()
