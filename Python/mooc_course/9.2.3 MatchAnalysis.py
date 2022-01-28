# 9.2.3 MatchAnalysis.py

from random import random

def printIntro():
    print('This program is designed to simluate matches between two players A and B')
    print('Abilities of two players are required(fractions between 0 and 1 exclusively)')

def getInputs():
    a = eval(input("Please key in the ability of playerA (0~1 exclusively):"))
    b = eval(input("Please key in the ability of playerB (0~1 exclusively):"))
    n = eval(input("Repeatition of simluations:"))
    return a, b, n

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Match analysis start, stimulate {} games in total".format(n))
    print("PlayerA won {} games, account for {:0.1%}".format(winsA, winsA/n))
    print("PlayerB won {} games, account for {:0.1%}".format(winsB, winsB/n))

def gameOver(a, b):
    return a == 15 or b == 15

def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB
                
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()