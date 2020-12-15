import math   
import copy

# def turnRight(facing, deg):
#     return facing + deg if facing + deg < 360 else (facing + deg) % 360

# def turnLeft(facing, deg):
#     return facing - deg if facing - deg >= 0 else 360 + facing - deg

# def getFacingDir(facing):
#     if facing == 0:
#         return [0, 1]
#     elif facing == 90:
#         return [1, 0]
#     elif facing == 180:
#         return [0, -1]
#     elif facing == 270:
#         return [-1, 0]

# def move(instr, current, facing):
#     key, dist = instr
    
#     if key == 'N':
#         current[1] += dist
#     elif key == 'E':
#         current[0] += dist
#     elif key == 'S':
#         current[1] -= dist
#     elif key == 'W':
#         current[0] -= dist
#     elif key == 'R':
#         return turnRight(facing, dist)
#     elif key == 'L':
#         return turnLeft(facing, dist)
#     elif key == 'F':
#         direction = getFacingDir(facing)
#         current[0] += direction[0] * dist
#         current[1] += direction[1] * dist
#     return facing

def move(instr, current, waypoint):
    key, dist = instr
    print(instr, current, waypoint)
    if key == 'N':
        waypoint[1] += dist
    elif key == 'E':
        waypoint[0] += dist
    elif key == 'S':
        waypoint[1] -= dist
    elif key == 'W':
        waypoint[0] -= dist
    elif key == 'R':
        rotate(current, waypoint, -dist)
    elif key == 'L':
        rotate(current, waypoint, dist)
    elif key == 'F':
        for _ in range(dist):
            relativeX = (waypoint[0] - current[0])
            relativeY = (waypoint[1] - current[1])
            current[0] += relativeX
            current[1] += relativeY
            waypoint[0] += relativeX
            waypoint[1] += relativeY
    

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    """

    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    point[0] = round(qx)
    point[1] = round(qy)

dirs = []
with open('12/input.txt') as f:
    while line := f.readline():
        line = line.strip("\n")
        dirs.append((line[0], int(line[1:])))


startPoint = [0, 0]
current = [0, 0]
waypoint = [10, 1]


for instr in dirs:
    move(instr, current, waypoint)

manhattan = (abs(current[0]) - startPoint[0]) + (abs(current[1]) - startPoint[1])
print(manhattan)


