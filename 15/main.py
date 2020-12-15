import math   
import copy
from itertools import product

with open('15/input.txt') as f:
    line = f.readline()
    start = list(map(int, line.strip("\n").split(",")))

track = {}
turn = 1
lastNum = 0

for num in start:
    track[lastNum] = turn - 1
    lastNum = num
    turn += 1

while True:

    if lastNum in track:
        nextNum = (turn - 1) - track[lastNum]
    else:
        nextNum = 0
        
    track[lastNum] = turn - 1

    if turn == 30000000:
        print(nextNum)
        break

    lastNum = nextNum
    turn += 1

    
        

        