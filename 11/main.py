import math


# leastCommonMultiple = 23 * 19 * 13 * 17
leastCommonMultiple = 3 * 5 * 2 * 13 * 11 * 17 * 19 * 7
# print(leastCommonDivisor)


class Monkey:
    def __init__(
        self, operand, worryMultiplier, divisibleBy, throwToIfTrue, throwToIfFalse
    ):
        self.items = []
        self.smallerItems = []
        # self.optItems = []
        self.operand = operand
        self.worryMultiplier = worryMultiplier
        self.divisibleBy = divisibleBy
        self.throwToIfTrue = throwToIfTrue
        self.throwToIfFalse = throwToIfFalse

        self.totalInspectedItems = 0

        self.topNumber = divisibleBy
        self.memory = {divisibleBy: True}

    def addItem(self, smallerItem):
        # self.items.append(item)
        self.smallerItems.append(smallerItem)

    # def addItemOpt(self, item):
    #     self.optItems.append()

    def updateWorryLevel(self, i):
        if self.operand == "+":
            # self.items[i] += (
            #     self.items[i]
            #     if self.worryMultiplier == "old"
            #     else int(self.worryMultiplier)
            # )
            self.smallerItems[i] += (
                self.smallerItems[i]
                if self.worryMultiplier == "old"
                else int(self.worryMultiplier)
            )
        elif self.operand == "*":
            # self.items[i] *= (
            #     self.items[i]
            #     if self.worryMultiplier == "old"
            #     else int(self.worryMultiplier)
            # )

            self.smallerItems[i] *= (
                self.smallerItems[i]
                if self.worryMultiplier == "old"
                else int(self.worryMultiplier)
            )

        # print(self.items[i], self.smallerItems[i], leastCommonMultiple)
        self.smallerItems[i] = self.smallerItems[i] % leastCommonMultiple

        # self.items[i] //= 3

    ## ((3*4*5+4)+5)*5*7
    # def updateWorryLevelOpt(self, i):
    #     if self.operand == "+":
    #         self.items[i].append(
    #             "+" + self.items[i]
    #             if self.worryMultiplier == "old"
    #             else "+" + self.worryMultiplier
    #         )
    #     elif self.operand == "*":
    #         self.items[i].append(
    #             "*" + self.items[i]
    #             if self.worryMultiplier == "old"
    #             else "*" + self.worryMultiplier
    #         )

    def throwToNextMonkey(self, i, allMonkeys):
        throwTo = None
        # bigNumber = self.items[i]
        smallNumber = self.smallerItems[i]
        # smallerNumber = 0
        # if self.topNumber <= bigNumber:
        #     smallerNumber = bigNumber - self.topNumber
        #     # print(self.topNumber)
        #     print(self.memory)
        #     throwTo = smallerNumber % self.divisibleBy == 0
        #     if throwTo:
        #         self.topNumber = bigNumber
        #         self.memory[bigNumber] = True
        #     # else:
        #     #     throwTo = False
        #     # self.memory[bigNumber] = throwTo

        if smallNumber % self.divisibleBy == 0:
            throwTo = True
        else:
            throwTo = False

        if throwTo:
            allMonkeys[self.throwToIfTrue].addItem(smallNumber)
        else:
            allMonkeys[self.throwToIfFalse].addItem(smallNumber)

    def inspectItems(self, allMonkeys):
        for i, item in enumerate(self.smallerItems):
            self.updateWorryLevel(i)
            self.throwToNextMonkey(i, allMonkeys)
            self.totalInspectedItems += 1

        # self.items = []
        self.smallerItems = []


input = []
with open("11/input.txt") as f:
    input = f.readlines()

input = [x.strip("\n") for x in input]

allMonkeys = []


i = 1
while True:
    if i >= len(input):
        break

    numbers = input[i].split(": ")[1]
    numbers = numbers.split(", ")
    numbers = list(map(int, numbers))

    operand = input[i + 1].split(" ")[-2]
    multiplier = input[i + 1].split(" ")[-1]
    divisibleBy = int(input[i + 2].split(" ")[-1])
    ifTrue = int(input[i + 3].split(" ")[-1])
    ifFalse = int(input[i + 4].split(" ")[-1])

    newMonkey = Monkey(operand, multiplier, divisibleBy, ifTrue, ifFalse)
    for num in numbers:
        newMonkey.addItem(num)
        # newMonkey.addItem(["+" + num])
    allMonkeys.append(newMonkey)

    i += 7

# for monkey in allMonkeys:
# print(
#     monkey.items,
#     monkey.operand,
#     monkey.worryMultiplier,
#     monkey.divisibleBy,
#     monkey.throwToIfTrue,
#     monkey.throwToIfFalse,
# )

for round in range(10000):
    if round % 100 == 0:
        print(round)
    for monkey in allMonkeys:
        # print(monkey.items)
        monkey.inspectItems(allMonkeys)


totalInspectedItems = []
for monkey in allMonkeys:
    totalInspectedItems.append(monkey.totalInspectedItems)

print(totalInspectedItems)

a = max(totalInspectedItems)
totalInspectedItems.remove(max(totalInspectedItems))
b = max(totalInspectedItems)
print(a)
print(b)
print(a * b)
