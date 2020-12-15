import math   
import copy

def convertToNum(x):
    return math.inf if x == "x" else int(x)

def getClosestAbove(busId, target):
    i = 1
    while True:
        if busId * i >= target:
            return busId * i - target
        i += 1


with open('13/input.txt') as f:
    timestamp = int(f.readline().strip("\n"))
    #busses = list(map(int,filter(lambda x: x != "x", f.readline().strip("\n").split(","))))
    busses = list(map(convertToNum, f.readline().strip("\n").split(",")))

# print(busses)


# closestList = [ getClosestAbove(x, timestamp) for x in busses ]
# print(closestList)
# smallest = min(closestList)

# indexOfClosest = closestList.index(smallest)
# closestId = busses[indexOfClosest]

# print(closestId)

# print(smallest * closestId)
# found = 0
# x = 7
# y = 13
# for i in range(0,10000, 7):
#     if (i + 1) % 13 == 0:
#         print(i, i//7, i+1, (i+1)//13)
#         found += 1
#         if found > 10:
#             break
    
offset = 0
#bussesChecked = []
currentAdder = 1
currentValidValue = 0

for bus in busses:
    print(bus, offset, currentAdder, currentValidValue)
    if bus == math.inf:
        offset += 1
        continue

    i = 1
    while True:
        candidate = currentValidValue + currentAdder * i
        if (candidate + offset) % bus == 0:
            currentAdder *= bus
            currentValidValue = candidate
            #print(candidate)
            break
        i += 1

    offset += 1
    
print(candidate)








