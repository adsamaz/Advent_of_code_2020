import math

arr = []
with open('2/input.txt') as f:
    arr = f.readlines()


def findValidPassword1():
    valid_count = 0
    for line in arr:
        rule, letter, password = line.split(" ")

        lower, upper = map(int, rule.split("-"))
        letter = letter[0]

        nrTimes = password.count(letter)
        if nrTimes >= lower and nrTimes <= upper:
            valid_count += 1
    return valid_count

def findValidPassword2():
    valid_count = 0
    for line in arr:
        rule, letter, password = line.split(" ")

        lower, upper = map(int, rule.split("-"))
        letter = letter[0]

        nrOccuring = 0
        if password[lower-1] == letter:
            nrOccuring += 1
        if password[upper-1] == letter:
            nrOccuring += 1
        
        if nrOccuring == 1:
            valid_count += 1
    return valid_count

print(findValidPassword2())



                



