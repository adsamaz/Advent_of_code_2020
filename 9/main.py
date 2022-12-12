import math


input = []
with open("9/input.txt") as f:
    input = f.readlines()

input = [x.strip("\n") for x in input]

# {'x-y': true}
allTailPositions = {}

# headPos = [0, 0]
# tailPos = [0, 0]

positions = [[0, 0] for _ in range(10)]
# print(positions)


def isTouching(head, tail):
    diffX = abs(head[0] - tail[0])
    diffY = abs(head[1] - tail[1])
    if diffX <= 1:
        return diffY <= 1
    if diffY <= 1:
        return diffX <= 1
    return False


def moveHead(direction):
    if direction == "R":
        positions[0][0] += 1
    if direction == "L":
        positions[0][0] -= 1
    if direction == "U":
        positions[0][1] += 1
    if direction == "D":
        positions[0][1] -= 1


def doMove(i):
    prev = positions[i - 1]
    curr = positions[i]
    if not isTouching(prev, curr):
        diffX = prev[0] - curr[0]
        diffY = prev[1] - curr[1]

        if diffX > 1:
            curr[0] += 1

            if diffY > 0:
                curr[1] += 1
            elif diffY < 0:
                curr[1] += -1

        elif diffX < -1:
            curr[0] += -1
            if diffY > 0:
                curr[1] += 1
            elif diffY < 0:
                curr[1] += -1

        elif diffY > 1:
            curr[1] += 1

            if diffX > 0:
                curr[0] += 1
            elif diffX < 0:
                curr[0] += -1

        elif diffY < -1:
            curr[1] += -1

            if diffX > 0:
                curr[0] += 1
            elif diffX < 0:
                curr[0] += -1

    if i == 9:
        allTailPositions[str(positions[i][0]) + "-" + str(positions[i][1])] = True


# 1
# for instr in input:
#     direction, steps = instr.split(" ")
#     for step in range(int(steps)):
#         doMove(direction)

# 2
for instr in input:
    direction, steps = instr.split(" ")
    for step in range(int(steps)):
        moveHead(direction)
        for i in range(1, len(positions)):
            doMove(i)

# print(allTailPositions.keys())

print(len(allTailPositions.keys()))
