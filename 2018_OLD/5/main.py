import math


with open('2018_OLD/5/input.txt') as f:
    line = f.readline()

i=0
while i < len(line) - 1:
    x = line[i]
    y = line[i+1]
    if x.lower() == y.lower():
        if x != y:
            line = line[:i] + line[i+2:]
            
            i = i-1 if i > 0 else i
            continue
        
    i += 1
        

print(len(line))