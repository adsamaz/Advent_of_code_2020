import math


input = []
with open("10/input.txt") as f:
    input = f.readlines()

input = [x.strip("\n") for x in input]


def addSignalStrength(cycle, register):
    if cycle in [20, 60, 100, 140, 180, 220]:
        print(cycle, register)
        return cycle * register
    return 0


spritePos = 0

register = 1
totalSum = 0
addAfterNextCycle = False
valueToAdd = 0

# 1
# for cycle in range(1, 221):

#     totalSum += addSignalStrength(cycle, register)

#     if addAfterNextCycle:
#         register += valueToAdd
#         valueToAdd = 0
#         addAfterNextCycle = False
#         continue

#     operation = input.pop(0)
#     if operation == "noop":
#         continue

#     op, num = operation.split(" ")
#     if op == "addx":
#         valueToAdd = int(num)
#         addAfterNextCycle = True


def getPixel(cycle):
    i = cycle % 40
    if cycle != 0 and i == 0:
        if spritePos == 38 or spritePos == 39 or spritePos == 40:
            return "#"
    if i == spritePos or i - 1 == spritePos or i - 2 == spritePos:
        return "#"
    return "."


arr = [["x" for _ in range(40)] for _ in range(6)]
# print(arr)
# 2
for cycle in range(1, 241):

    # print(cycle // 40, cycle % 40, spritePos)
    # print((cycle - 1) // 40, (cycle - 1) % 40, getPixel(cycle), spritePos)
    arr[(cycle - 1) // 40][(cycle - 1) % 40] = getPixel(cycle)

    if addAfterNextCycle:
        register += valueToAdd
        spritePos = register
        valueToAdd = 0
        addAfterNextCycle = False
        continue

    operation = input.pop(0)
    if operation == "noop":
        continue

    op, num = operation.split(" ")
    if op == "addx":
        valueToAdd = int(num)
        addAfterNextCycle = True

print(["".join(a) for a in arr])
