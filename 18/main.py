import math   
import copy
from itertools import product

def getSum(expr):
    acc = 0
    op = "+"
    i = 0
    while i < len(expr):
        char = expr[i]
        if char.isdigit():
            if op == "+":
                acc += int(char)
            elif op == "*":
                acc *= int(char)
            i += 1
        elif char == " ":
            i += 1
            continue
        elif char == "+":
            i += 1
            op = "+"
        elif char == "*":
            i += 1
            op = "*"
        elif char == "(":
            if op == "+":
                partSum, steps = getSum(expr[i+1:])
                acc += partSum
                i += steps + 2
            elif op == "*":
                partSum, steps = getSum(expr[i+1:])
                acc *= partSum
                i += steps + 2
        elif char == ")":
            return acc, i
        else:
            raise Exception("Unhandled char: " + char)
    return acc, i

    
def getSum2(expr):
    acc = 0
    op = "+"
    i = 0
    while i < len(expr):
        char = expr[i]
        if char.isdigit():
            if op == "+":
                acc += int(char)
            elif op == "*":
                acc *= int(char)
            i += 1
        elif char == " ":
            i += 1
            continue
        elif char == "+":
            i += 1
            op = "+"
        elif char == "*":
            op = "*"
            partSum, steps = getSum2(expr[i+1:])
            return acc * partSum, i+1 + steps
        elif char == "(":
            if op == "+":
                partSum, steps = getSum2(expr[i+1:])
                acc += partSum
                i += steps + 2
            elif op == "*":
                partSum, steps = getSum2(expr[i+1:])
                acc *= partSum
                i += steps + 2
        elif char == ")":
            return acc, i
        else:
            raise Exception("Unhandled char: " + char)
    return acc, i



with open('18/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    
    totalSum = 0
    for line in lines:
        totalSum += getSum2(line)[0]


print(totalSum)




