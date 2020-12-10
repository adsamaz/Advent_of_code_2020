import math   
import copy

numbers = []
with open('10/input.txt') as f:
    while line := f.readline():
        line = line.strip("\n")
        numbers.append(int(line))
    numbers = sorted(numbers)

# Part1
# def traverseAdapters(numbers):
#     obj = {1:0, 2:0, 3:0}

#     current = 0
#     for i, x in enumerate(numbers):
#         diff = x - current
#         obj[diff] += 1
#         current = x
    
#     # End
#     obj[3] += 1
#     return obj

# Part 2
# Dynamic programming
# { 0: 2}
foundValues = {}

def recc(nums):
    if len(nums) == 1:
        return 1
    curr = nums[0]
    
    if curr in foundValues:
        return foundValues[curr]

    if len(nums) > 3 and nums[3] - curr <= 3:
        res = 0+recc(nums[1:]) + recc(nums[2:]) + recc(nums[3:])
        foundValues[curr] = res
        return res
    elif len(nums) > 2 and nums[2] - curr <= 3:
        res = 0+recc(nums[1:]) + recc(nums[2:])
        foundValues[curr] = res
        return res
    elif len(nums) > 1 and nums[1] - curr <= 3:
        res = recc(nums[1:])
        foundValues[curr] = res
        return res
    
    

numbers.insert(0, 0)
result = recc(numbers)

print(result)



                



