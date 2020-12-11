import math   
import copy

grid = []
with open('11/input.txt') as f:
    while line := f.readline():
        line = line.strip("\n")
        grid.append(line)


def checkAndReplace(i, j, grid):
    seat = grid[i][j]
    if seat == ".":
        return "."

    seatsToTest = [(i,j+1), (i+1,j+1), (i+1,j), (i+1,j-1), (i,j-1), (i-1,j-1), (i-1,j), (i-1,j+1)]

    if seat == "L":
        for x, y in seatsToTest:
            if x < 0 or y < 0:
                continue
            try:
                if grid[x][y] == "#":
                    return "L"
            except:
                continue
        return "#"
    
    if seat == "#":
        count = 0
        for x, y in seatsToTest:
            if x < 0 or y < 0:
                continue
            try:
                #print(grid[x][y], x, y)
                if grid[x][y] == "#":
                    count += 1
            except:
                continue
        #print(count)
        return "L" if count >= 4 else "#"

def getClosest(i,j,x,y,grid):
    while True:
        i += x
        j += y
        if i < 0 or j < 0:
            raise IndexError 
        if grid[i][j] != ".":
            return grid[i][j]


def checkAndReplace2(i, j, grid):
    seat = grid[i][j]
    if seat == ".":
        return "."

    direction = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    
    if seat == "L":
        for x, y in direction:
            
            try:
                closestSeatType = getClosest(i,j,x,y,grid)
                if closestSeatType == "#":
                    return "L"
            except:
                continue
        return "#"
    
    if seat == "#":
        count = 0
        for x, y in direction:

            try:
                #print(i,j,x,y)
                closestSeatType = getClosest(i,j,x,y,grid)
                if closestSeatType == "#":
                    count += 1
            except:
                continue
        #print(count)
        return "L" if count >= 5 else "#"

def changeGrid(grid):
    newGrid = [["" for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            newGrid[i][j] = checkAndReplace2(i, j, grid)

    for i, x in enumerate(newGrid):
        newGrid[i] = "".join(x)

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
            if y == "#":
                count += 1
    return count

def run(grid):
    prevGrid = [[] for _ in range(len(grid))]

    while not deepEquals(grid, prevGrid):
        prevGrid = grid[:]
        grid = changeGrid(grid)

    print(findOccupied(grid))

#grid = grid[:2]
print(grid)
run(grid)