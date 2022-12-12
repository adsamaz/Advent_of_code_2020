import math

arr = []
with open("1\input.txt") as f:
    arr = f.readlines()

arr = list(map(int, arr))


def findIncreasing(arr):
    count = 0
    for i, x in enumerate(arr[1:]):
        if x > arr[i]:
            count += 1
    return count


# Only need to compare at the first number of the window and the last number of the new window.
# The two numbers in the middle are shared by both windows
def findIncreasingThree(arr):
    count = 0
    for i, x in enumerate(arr):
        if i < 3:
            continue
        if x > arr[i - 3]:
            count += 1
    return count


print(findIncreasingThree(arr))
