import math

grid = []
with open('3/input.txt') as f:
    while line := f.readline():
        arrRow = [x for x in line]
        if arrRow[-1] == '\n':
            del arrRow[-1] # delete newline

        extendedArrRow = []
        for i in range(100):
            extendedArrRow.extend(arrRow)

        grid.append(extendedArrRow)
    

# Traverse
def traverse(addY, addX):
    nrTrees = 0
    x = 0
    y = 0
    while y < len(grid):
        nrTrees += 1 if grid[y][x] == '#' else 0
        x += addX
        y += addY
    print(nrTrees)
    return nrTrees

result = traverse(1,1)*traverse(1,3)*traverse(1,5)*traverse(1,7)*traverse(2,1)  

print(result)



                



