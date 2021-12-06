import math

arr = []
with open("2/input.txt") as f:
    arr = f.readlines()


def calcPosition(arr):
    horizontal = 0
    depth = 0
    for line in arr:
        dir, value = line.split(" ")

        if dir == "forward":
            horizontal += int(value)
        if dir == "down":
            depth += int(value)
        if dir == "up":
            depth -= int(value)

    return horizontal * depth


def calcPosition2(arr):
    horizontal = 0
    depth = 0
    aim = 0
    for line in arr:
        dir, value = line.split(" ")

        if dir == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        if dir == "down":
            aim += int(value)
        if dir == "up":
            aim -= int(value)

    return horizontal * depth


print(calcPosition2(arr))
