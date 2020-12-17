import math   
import copy
import itertools

l = 32
row = ["." for _ in range(l)]
twoDRow = [copy.deepcopy(row) for _ in range(l)]
threeDRow = [copy.deepcopy(twoDRow) for _ in range(l)]
grid = [copy.deepcopy(threeDRow) for _ in range(l)]

with open('17/input.txt') as f:
    
    for index, line in enumerate(f.readlines()):
        line = line.strip("\n")

        inputLength = len(line)
        i = l - (l//2 - inputLength//2) + index
        j = l - (l//2 - inputLength//2)

        for char in line:
            grid[l//2][l//2][i][j] = char
            j += 1

def checkAndReplace2(i, j, k, m, grid):
    seat = grid[i][j][k][m]

    direction = list(itertools.product([-1,0,1], repeat=4))
    direction.remove((0,0,0,0))
    
    if seat == "#":
        count = 0
        for x, y, z, w in direction:
            try:
                if grid[i+x][j+y][z+k][w+m] == "#":
                    count += 1
            except:
                continue
        return "#" if count in [2, 3] else "."
    
    if seat == ".":
        count = 0
        for x, y, z, w in direction:
            try:
                if grid[i+x][j+y][z+k][w+m] == "#":
                    count += 1
            except:
                continue
        return "#" if count == 3 else "."

def changeGrid(grid):
    row = ["." for _ in range(l)]
    twoDRow = [copy.deepcopy(row) for _ in range(l)]
    threeDRow = [copy.deepcopy(twoDRow) for _ in range(l)]
    newGrid = [copy.deepcopy(threeDRow) for _ in range(l)]

    for m, w in enumerate(grid):
        for k, z in enumerate(w):
            for i, x in enumerate(z):
                for j, y in enumerate(x):
                    newGrid[m][k][i][j] = checkAndReplace2(m, k, i, j, grid)
    return newGrid
    

# List of strings
def deepEquals(g1, g2):
    for i, x in enumerate(g1):
        if x != g2[i]:
            return False
    return True

def findOccupied(grid):
    count = 0
    for x in grid:
        for y in x:
            for z in y:
                for w in z:
                    if w == "#":
                        count += 1
    return count

def run(grid):

    for i in range(6):
        grid = changeGrid(grid)

    print(findOccupied(grid))

run(grid)
