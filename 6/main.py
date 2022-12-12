import math


string = ""
with open("6/input.txt") as f:
    string = f.readline()


def isDifferent(a, b, c, d):
    if a == b or b == c or c == d or a == d or a == c or b == d:
        return False
    return True


def isDifferentBig(arr):
    for i, a in enumerate(arr):
        for b in arr[:i] + arr[i + 1 :]:
            if a == b:
                return False
    return True


# for i, x in enumerate(string):
#     if isDifferent(*string[i : i + 4]):
#         print(i + 4)
#         break

# 2
for i, x in enumerate(string):
    if isDifferentBig(string[i : i + 14]):
        print(i + 14)
        break

# print(string)
