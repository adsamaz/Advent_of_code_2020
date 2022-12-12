import math

input = []
with open("12/input.txt") as f:
    input = f.readlines()

input = [x.strip("\n") for x in input]


def getStepsInDirection(grid, i, j, current, visited):
    if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
        return 0

    new = "a" if grid[i][j] == "S" else grid[i][j]

    if new != "E":
        if str(i) + str(j) in visited:
            return 0

    if new == "E":
        return 1 if current == "y" or current == "z" else 0
    if ord(new) <= ord(current) + 1:
        valueFromDir = getStepsToE(grid, i, j, visited)
        return valueFromDir + 1 if valueFromDir > 0 else 0
    return 0


def getStepsToE(grid, i, j, visited):
    current = "a" if grid[i][j] == "S" else grid[i][j]
    # print(i, j, current)
    visited[str(i) + str(j)] = True

    dirs = list(
        filter(
            lambda x: x > 0,
            [
                getStepsInDirection(grid, i, j + 1, current, visited.copy()),
                getStepsInDirection(grid, i, j - 1, current, visited.copy()),
                getStepsInDirection(grid, i + 1, j, current, visited.copy()),
                getStepsInDirection(grid, i - 1, j, current, visited.copy()),
            ],
        )
    )
    return 0 if len(dirs) == 0 else min(dirs)


def getStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return (i, j)


start = getStart(input)

print(input)
steps = getStepsToE(input, *start, {})

print(steps)
