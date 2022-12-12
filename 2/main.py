import math


def getPoints(opp, me):
    if opp == "A":
        if me == "X":
            return 1 + 3
        if me == "Y":
            return 2 + 6
        if me == "Z":
            return 3 + 0
    if opp == "B":
        if me == "X":
            return 1 + 0
        if me == "Y":
            return 2 + 3
        if me == "Z":
            return 3 + 6
    if opp == "C":
        if me == "X":
            return 1 + 6
        if me == "Y":
            return 2 + 0
        if me == "Z":
            return 3 + 3


def getPoints2(opp, outcome):
    if opp == "A":
        if outcome == "X":
            return 3 + 0
        if outcome == "Y":
            return 1 + 3
        if outcome == "Z":
            return 2 + 6
    if opp == "B":
        if outcome == "X":
            return 1 + 0
        if outcome == "Y":
            return 2 + 3
        if outcome == "Z":
            return 3 + 6
    if opp == "C":
        if outcome == "X":
            return 2 + 0
        if outcome == "Y":
            return 3 + 3
        if outcome == "Z":
            return 1 + 6


arr = []
with open("2\input.txt") as f:
    arr = f.readlines()


obj = [(x.split(" ")[0], x.split(" ")[1].strip("\n")) for x in arr]

sum = 0
for round in range(len(obj)):
    elem = obj[round]
    sum += getPoints2(*elem)

print(sum)
