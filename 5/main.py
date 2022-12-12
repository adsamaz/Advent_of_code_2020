import math


arr = []
with open("5/creates.txt") as f:
    arr = f.readlines()

stacks = [x.split(" ") for x in arr]

newStacks = [[] for _ in range(len(stacks) + 1)]
for array in stacks:
    i = 0
    while i < len(array):
        # print(newStacks)
        if array[i] == "":
            array = array[:i] + array[i + 3 :]
        else:
            newStacks[i].append(array[i][1])
        i += 1

for stack in newStacks:
    stack.reverse()

stacks = newStacks
# print(newStacks)

commands = []
with open("5/input.txt") as f:
    commands = f.readlines()


commands = [
    list(
        map(
            int,
            filter(lambda y: y not in ["from", "move", "to"], x.strip("\n").split(" ")),
        )
    )
    for x in commands
]

# for (num_creates, fro, to) in commands:
#     for _ in range(num_creates):
#         # print(stacks)
#         stacks[to - 1].append(stacks[fro - 1].pop())

# 2
for (num_creates, fro, to) in commands:
    creates = []
    for _ in range(num_creates):
        creates.append(stacks[fro - 1].pop())
    creates.reverse()
    stacks[to - 1].extend(creates)

print(stacks)

string = ""
for stack in stacks:
    string += stack[len(stack) - 1]

print(string)
