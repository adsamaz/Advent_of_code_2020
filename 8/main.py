import math   
import copy

program = []
with open('8/input.txt') as f:
    while line := f.readline():
        
        op, offset = line.split(" ")
        offset = int(offset)
        program.append([op, offset])

def run(program):
    p = 0
    acc = 0
    saveP = {}
    while p < len(program):
        if p in saveP:
            #print(acc)
            return
        saveP[p] = 1

        op, offset = program[p]
        if op == "acc":
            acc += offset
            p += 1
        elif op == "jmp":
            p += offset
        elif op == "nop":
            p += 1
    print(acc)
    return acc

i = 0
print(program)
while True:
    cProgram = copy.deepcopy(program)
    #print(cProgram)
    #print(copy[i])
    if cProgram[i][0] == "jmp":
        cProgram[i][0] = "nop"
    elif cProgram[i][0] == "nop":
        cProgram[i][0] = "jmp"
    
    result = run(cProgram)
    #print(result)
    if result == None:
        i += 1  
    else:
        print(result)
        break
        
        





                



