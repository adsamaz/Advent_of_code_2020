import math


def containsAll(a, b):
    for x in a:
        if not x in b:
            return False
    return True


def containsSome(a, b):
    for x in a:
        if x in b:
            return True
    return False


arr = []
with open("4/input.txt") as f:
    arr = f.readlines()

arr = [x.strip("\n") for x in arr]
arr = [x.split(",") for x in arr]
arr = [[int(x.split("-")[0]), int(x.split("-")[1])] for y in arr for x in y]


total = 0
for i, (a, b) in enumerate(arr):
    if i % 2 != 0:
        continue

    range1 = list(range(a, b + 1))
    range2 = list(range(arr[i + 1][0], arr[i + 1][1] + 1))
    # print(range1, range2)

    # if containsAll(range1, range2) or containsAll(range2, range1):
    #     total += 1

    # 2
    if containsSome(range1, range2) or containsSome(range2, range1):
        total += 1


print(total)
