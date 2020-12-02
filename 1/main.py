import math

arr = []
with open('input.txt') as f:
    arr = f.readlines()

arr = list(map(int, arr))

def findTwoNumbers(arr, goal):
    for i, x in enumerate(arr):
        for y in arr[i:]:
            if x + y == goal:
                return (x, y)
    return (0, 0)

def findThreeNumbers(arr, goal):
    for i, x in enumerate(arr):
        foundX, foundY = findTwoNumbers(arr[:i], goal - x)
        if foundX > 0 and foundY > 0:
            return x * foundX * foundY

print(findThreeNumbers(arr, 2020))


                



