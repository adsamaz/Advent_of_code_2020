arr = [x for x in range(1, 10) if x % 2 == 0]

arr = [
    (x, y) for x in range(0, 10) for y in range(0, 10) if x % 2 == 0 and not y % 2 == 0
]

print(arr)
