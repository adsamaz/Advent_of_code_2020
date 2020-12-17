import math   
import copy
import itertools
#import product from itertools

l = 30
row = ["." for _ in range(l)]
twoDRow = [copy.deepcopy(row) for _ in range(l)]
grid = [copy.deepcopy(twoDRow) for _ in range(l)]

with open('17/input.txt') as f:
    
    for index, line in enumerate(f.readlines()):
        line = line.strip("\n")

        inputLength = len(line)
        i = l - (l//2 - inputLength//2) + index
        j = l - (l//2 - inputLength//2)

        for char in line:
            grid[l//2][i][j] = char
            #print(char, i, j)
            j += 1


def checkAndReplace2(i, j, k, grid):
    seat = grid[i][j][k]

    direction = list(itertools.product([-1,0,1], repeat=3))
    direction.remove((0,0,0))
    #print(direction)
    
    if seat == "#":
        count = 0
        for x, y, z in direction:
            try:
                #seatInDir = (i+x, j+y, k+z)
                if grid[i+x][j+y][z+k] == "#":
                    count += 1
            except:
                continue
        return "#" if count in [2, 3] else "."
    
    if seat == ".":
        count = 0
        for x, y, z in direction:
            try:
                #seatInDir = (i+x, j+y, k+z)
                if grid[i+x][j+y][z+k] == "#":
                    count += 1
            except:
                continue
        return "#" if count == 3 else "."

def changeGrid(grid):
    row = ["" for _ in range(l)]
    twoDRow = [copy.deepcopy(row) for _ in range(l)]
    newGrid = [copy.deepcopy(twoDRow) for _ in range(l)]

    for k, z in enumerate(grid):
        for i, x in enumerate(z):
            for j, y in enumerate(x):
                newGrid[k][i][j] = checkAndReplace2(k, i, j, grid)

    #for i, x in enumerate(newGrid):
    #    newGrid[i] = "".join(x)

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
                if z == "#":
                    count += 1
    return count

def run(grid):
    #prevGrid = [[[] for _ in range(len(grid))] for _ in range(len(grid))]

    for i in range(6):
        #prevGrid = copy.deepcopy(grid)
        grid = changeGrid(grid)

    print(findOccupied(grid))
    #print(grid)
#grid = grid[:2]
#print(grid)

run(grid)