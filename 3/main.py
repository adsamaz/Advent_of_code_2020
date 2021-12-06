import math

arr = []
with open("3/input.txt") as f:
    arr = f.readlines()

# 1
def calc(arr):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in arr:
        for i, bit in enumerate(line):

            if bit == "1":
                result[i] += 1
            if bit == "0":
                result[i] -= 1

    return result


def calc_gamma(arr):
    binaryString = ""
    for num in arr:
        if num > 0:
            binaryString += "1"
        if num < 0:
            binaryString += "0"

    return int(binaryString, 2)


def calc_epsilon(arr):
    binaryString = ""
    for num in arr:
        if num > 0:
            binaryString += "0"
        if num < 0:
            binaryString += "1"

    return int(binaryString, 2)


# 2
def calcBitDensity(arr):
    result = [0 for _ in arr[0]]
    for line in arr:
        for i, bit in enumerate(line):

            if bit == "1":
                result[i] += 1
            if bit == "0":
                result[i] -= 1

    return result


def calc_gamma(arr):
    binaryString = ""
    for num in arr:
        if num > 0:
            binaryString += "1"
        if num < 0:
            binaryString += "0"

    return int(binaryString, 2)


def calc_epsilon(arr):
    binaryString = ""
    for num in arr:
        if num > 0:
            binaryString += "0"
        if num < 0:
            binaryString += "1"

    return int(binaryString, 2)


def getOGR(arr):
    currentArr = arr.copy()
    i = 0
    while len(currentArr) > 1:
        density = calcBitDensity(currentArr)

        if density[i] >= 0:
            currentArr = [line for line in currentArr if line[i] == "1"]
        if density[i] < 0:
            currentArr = [line for line in currentArr if line[i] == "0"]

        i += 1
    return int(currentArr[0], 2)


def getCO2(arr):
    currentArr = arr.copy()
    i = 0
    while len(currentArr) > 1:
        density = calcBitDensity(currentArr)

        if density[i] >= 0:
            currentArr = [line for line in currentArr if line[i] == "0"]
        if density[i] < 0:
            currentArr = [line for line in currentArr if line[i] == "1"]

        i += 1
    return int(currentArr[0], 2)


print(getCO2(arr) * getOGR(arr))
