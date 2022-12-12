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


def findSameLetter(a, b):
    for letter in a:
        for letter2 in b:
            if letter == letter2:
                return letter


def findSameLetter3(a, b, c):
    for letter in a:
        for letter2 in b:
            for letter3 in c:
                if letter == letter2 and letter2 == letter3:
                    return letter


arr = []
with open("3/input.txt") as f:
    arr = f.readlines()

arr = [x.strip("\n") for x in arr]
# comps = [(x[len(x) // 2 :], x[: len(x) // 2]) for x in arr]

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pointsMapper = {letters[v - 1]: v for v in range(1, 53)}

# sum = 0
# for sack in comps:
#     letter = findSameLetter(*sack)
#     sum += pointsMapper[letter]


# 2
groups = [(arr[i], arr[i + 1], arr[i + 2]) for i in range(0, len(arr), 3)]

sum = 0
for sack in groups:
    letter = findSameLetter3(*sack)
    sum += pointsMapper[letter]


print(sum)
