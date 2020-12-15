import math   
import copy
from itertools import product

def bin36ToInt(valArr):
    result = 0
    i = 0
    for val in reversed(valArr):
        result += val * (2**i)
        i += 1
    return result

def replaceValue(mask, value):
    valStr = "%036d" % int(bin(value)[2:])
    valArr = [int(val) for val in valStr]

    resultArr = []
    for m, v in zip(mask, valArr):
        resultArr.append(v if m == "X" else int(m))

    return bin36ToInt(resultArr)

def replaceKey(mask, key):
    keyStr = "%036d" % int(bin(key)[2:])
    keyArr = [int(val) for val in keyStr]

    resultArr = []
    for m, v in zip(mask, keyArr):
        if m == "X":
            resultArr.append("X")
        elif m == "1":
            resultArr.append(1)
        elif m == "0":
            resultArr.append(int(v))
    return resultArr

def findAllKeys(key):
    xCount = key.count("X")
    allCombs = list(product([0,1], repeat=xCount))
    #print(allCombs)
    newKeys = []
    for comb in allCombs:
        currentKey = key[:]
        combIndex = 0
        for i, bit in enumerate(key):
            if bit == "X":
                currentKey[i] = comb[combIndex]
                combIndex += 1
        newKeys.append(bin36ToInt(list(map(int, currentKey))))
    return newKeys


mem = {}
mask = []
with open('14/input.txt') as f:
    while line := f.readline():
        instr, value = line.strip("\n").split("=")
        instr = instr.strip()
        value = value.strip()

        if instr == "mask":
            mask = [val for val in value]
        else:
            key = int(instr.split("[")[1].strip("]"))
            value = int(value)
            newKeyArr = replaceKey(mask, key)
            allKeys = findAllKeys(newKeyArr)

            #print(allKeys)

            for k in allKeys:
                mem[k] = value

totSum = 0
for key in mem.keys():
    totSum += mem[key]

print(totSum)







