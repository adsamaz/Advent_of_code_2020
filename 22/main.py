import math   
import copy
from itertools import product

with open('22/p1.txt') as f:
    p1 = [int(x.strip()) for x in f.readlines()]

with open('22/p2.txt') as f:
    p2 = [int(x.strip()) for x in f.readlines()]



def calcResult(arr):
    result = 0
    for i, x in enumerate(arr):
        result += (len(arr) - i) * x
        #print((len(arr) - i))
    return result

# PART 1
# while True:
#     if len(p1) == 0:
#         #print(p2)
#         print(calcResult(p2))
#         break
#     if len(p2) == 0:
#         print(calcResult(p1))
#         break
#     card1 = p1.pop(0)
#     card2 = p2.pop(0)
#     if card1 > card2:
#         p1.extend([card1, card2])
#     else:
#         p2.extend([card2, card1])



globCount = 1
globMemory = {}
def recGame(p1, p2):
    #print(",".join(map(str, p1)) + "+" + ",".join(map(str, p2)))
    if ",".join(map(str, p1)) + "+" + ",".join(map(str, p2)) in globMemory:
        print("found one")
        #print("HJE")
        return globMemory[",".join(map(str, p1)) + "+" + ",".join(map(str, p2))]
    memory = {}
    while True:
        if ",".join(map(str, p1)) + "+" + ",".join(map(str, p2)) in memory:
            print("Aborting, same memoy found, p1 winns")
            return "p1", p1[:]
        else:
            saveP1 = p1[:]
            saveP2 = p2[:]

        if len(p1) == 0:
            return "p2", p2[:]
        elif len(p2) == 0:
            return "p1", p1[:]
        
        card1 = p1.pop(0)
        card2 = p2.pop(0)
        #print(card1, card2)
        #print(p1, p2)
        if card1 <= len(p1) and card2 <= len(p2):
            #print("Entering reccursive combat")
            if ",".join(map(str, p1)) + "+" + ",".join(map(str, p2)) in globMemory:
                winner, arr = globMemory[",".join(map(str, p1)) + "+" + ",".join(map(str, p2))]
            else:
                winner, arr = recGame(p1[:], p2[:])

            if winner == "p1":
                #print("p1 winns after reccursive combat")
                p1.extend([card1, card2])
                winDeck = p1
            elif winner == "p2":
                #print("p2 winns after reccursive combat")
                p2.extend([card2, card1])
                winDeck = p2
        else:
            if card1 > card2:
                #print("p1 winns")
                p1.extend([card1, card2])
                winner = "p1"
                winDeck = p1
            else:
                #print("p2 winns")
                p2.extend([card2, card1])
                winner = "p2"
                winDeck = p2

        memory[",".join(map(str, p1[:])) + "+" + ",".join(map(str, p2[:]))] = winner, winDeck[:]
        globMemory[",".join(map(str, p1[:])) + "+" + ",".join(map(str, p2[:]))] = winner, winDeck[:]

        

winner, deck = recGame(p1, p2)
result = calcResult(deck)
print(p1, p2)

print(winner, result)
