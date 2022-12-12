import math


opts = []
with open("7/input.txt") as f:
    opts = f.readlines()

opts = [x.strip("\n") for x in opts]

system = {"/": {}}
currentPath = ["/"]


def getCurrentSubSystem(system, path):
    # if len(path) == 1:
    #     system = {"/": subSystem}
    # else:

    curr = system[path[0]]
    for p in path[1:]:
        curr = curr[p]
    return curr


for i, opt in enumerate(opts):
    if opt[0] == "$":
        if opt[2:4] == "cd":
            # print("cd")
            if opt[5] == "/":
                currentPath = ["/"]
            elif opt[5:7] == "..":
                currentPath.pop()
            else:
                currentPath.append(opt[5:])

        if opt[2:4] == "ls":
            # print("ls")
            objects = []
            for obj in opts[i + 1 :]:
                if (obj[0]) == "$":
                    break
                else:
                    objects.append(obj)

            for x in objects:
                key = x[4:] if x[0] == "d" else x.split(" ")[1]
                value = {} if x[0] == "d" else x.split(" ")[0]
                subSystem = getCurrentSubSystem(system, currentPath)
                subSystem[key] = value

            # Ehh
            # setCurrentSubSystem(system, currentPath, subSystem)
    else:
        continue

globalTotal = []


# def getFileSize(sys):
#     total = 0
#     for key, value in sys.items():
#         if type(value) is dict:
#             dictSize = getFileSize(value)
#             total += dictSize
#         else:
#             total += int(value)

#     if total <= 100000:
#         print("hej", total)
#         globalTotal.append(total)
#     return total


# 2
def getFileSize2(sys):
    total = 0
    for key, value in sys.items():
        if type(value) is dict:
            dictSize = getFileSize2(value)
            total += dictSize
        else:
            total += int(value)

    if total >= 30000000 - (70000000 - 46728267):
        print("hej", total)
        globalTotal.append(total)
    return total


size = getFileSize2(system)
print(size, min(globalTotal))
