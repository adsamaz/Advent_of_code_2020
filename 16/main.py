import math   
import copy
from itertools import product, combinations, permutations


def checkRules(x, rules):
    valiedCategories = []
    
    for rule in rules:
        #print(rule)
        if x >= rule[1][0] and x <= rule[1][1]:
            valiedCategories.append(rule[0])
    return valiedCategories

rules = []
allCategories = {}
with open('16/input.txt') as f:
    line = [x.strip("\n") for x in f.readlines()]
    for l in line:
        if len(l.split(" ")) == 4:
            category, first, _, second = l.split(" ")
            rules.append((category, list(map(int, first.split("-")))))
            rules.append((category, list(map(int, second.split("-")))))
            allCategories[category] = 1
        elif len(l.split(" ")) == 5:
            category1, category2, first, _, second = l.split(" ")
            rules.append((category1 + category2, list(map(int, first.split("-")))))
            rules.append((category1 + category2, list(map(int, second.split("-")))))
            allCategories[category1 + category2] = 1
    
with open('16/inputTickets.txt') as f:
    line = [x.strip("\n") for x in f.readlines()]
    
    rowMap = {}
    invalid = 0
    for l in line:
        for row, x in enumerate(l.split(",")):
            categories = checkRules(int(x), rules)
            if len(categories) == 0:
                invalid += int(x)
                continue
            
            if row in rowMap:
                rowMap[row].append(categories)
            else:
                rowMap[row] = [categories]
            

    candidatesPerRow = {}
    for key in rowMap.keys():
        candidates = allCategories.copy()
        for i, categories in enumerate(rowMap[key]):
            for j, cat in enumerate(allCategories.keys()):
                if cat not in categories:
                    if cat in candidates:
                        del candidates[cat]
        candidatesPerRow[key] = candidates


    sortedArr = sorted([(key, list(obj.keys())) for key, obj in candidatesPerRow.items()], key=(lambda a: len(a[1])))

    finalObject = {}
    for nr, cats in sortedArr:
        thisCat = [e for e in cats if e not in finalObject].pop()
        finalObject[thisCat] = nr

    myTicket = [97,101,149,103,137,61,59,223,263,179,131,113,241,127,53,109,89,173,107,211]

    resultProduct = 1
    for cat, index in finalObject.items():
        if "departure" in cat:
            resultProduct *= myTicket[index]

    print(resultProduct)
        
        
            


