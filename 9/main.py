import math   
import copy

numbers = []
with open('9/input.txt') as f:
    while line := f.readline():
        line = line.strip("\n")
        numbers.append(int(line))

def findTwoPrev(val, prevArr):
    for i, x in enumerate(prevArr):
        for j, y in enumerate(prevArr):
            if x + y == val and i != j:
                return True
    return False

def findNCont(val, prevArr):
    for i, x in enumerate(prevArr):
        candidates = [x]
        currentSum = x

        for j, y in enumerate(prevArr[i+1:]):
            if currentSum + y == val:
                candidates.append(y)
                return candidates
            
            if currentSum + y > val:
                break
                
            candidates.append(y)
            currentSum += y

    print("Fail")

# Part 1
#
# for i, x in enumerate(numbers):
#     if i < 25:
#         continue

#     if findTwoPrev(x, numbers[i-25:i]):
#         continue
#     else:
#         print(x)
#         break
        
foundNumber = 2089807806
foundIndex = numbers.index(foundNumber)
# Part 2

result = findNCont(foundNumber, numbers[:foundIndex])

print(max(result) + min(result))




                



