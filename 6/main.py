import math


with open("6/input.txt") as f:
    fishes = list(map(int, f.readline().split(",")))

fishMap = {num: fishes.count(num) for num in fishes}
fishMap[0] = 0
fishMap[6] = 0
fishMap[7] = 0
fishMap[8] = 0
print(fishMap)


# def getUpdatedFish(fish):
#     if fish == 0:
#         return [6, 8]
#     return [fish - 1]


# def run1(fishes: list):
#     for day in range(256):
#         print(day)
#         updatedFishes = []
#         for fish in fishes:
#             updatedFishes.extend(getUpdatedFish(fish))
#         fishes = updatedFishes
#     return fishes


def updateFishMap(fishMap: "dict[int,int]"):
    newMap = {}
    for i in reversed(range(9)):
        if i == 0:
            newMap[6] += fishMap[0]
            newMap[8] = fishMap[0]
        else:

            newMap[i - 1] = fishMap[i]
    return newMap


def run2(fishMap: "dict[int,int]"):
    for day in range(256):
        fishMap = updateFishMap(fishMap)
    return fishMap


updatedFishes = run2(fishMap)
print(sum([val for val in updatedFishes.values()]))
