import math

def getCorrectHeight(h):
    try:
        height = int(h[:-2])
        measure = h[-2:]
    except:
        return False
    if measure == 'cm':
        return height <= 193 and height >= 150
    if measure == "in":
        return height <= 76 and height >= 59
    return False

def getCorrectHairColor(h):
    if not h[0] == "#":
        return False
    
    rest = h[1:]
    if not len(rest) == 6:
        return False

    r = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    return all(e in r for e in rest)

def getCorrectEyeColor(h):
    r = ['amb', 'blu','brn', 'gry', 'grn', 'hzl', 'oth']
    return h in r

def getCorrectPid(h:str):
    if len(h) != 9: return False
    for i in h:
        if not i.isdigit():
            return False
    return True


validKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid
def isValid(passport):
    keys = passport.keys()
    if all(e in keys for e in validKeys):
        return 1 if int(passport['byr']) <= 2002 and int(passport['byr']) >= 1920 and \
            int(passport['iyr']) <= 2020 and int(passport['iyr']) >= 2010 and \
             int(passport['eyr']) <= 2030 and int(passport['eyr']) >= 2020 and \
              getCorrectHeight(passport['hgt']) and \
                getCorrectHairColor(passport['hcl']) and \
                 getCorrectEyeColor(passport['ecl']) and \
                  getCorrectPid(passport['pid']) \
                    else 0
    return 0

with open('4/input.txt') as f:
    passport = {}
    valid = 0
    while line := f.readline():
        
        if line == "\n":
            valid += isValid(passport)
            #if isValid(passport):
                #print(passport)
            passport = {}
            continue

        arr = line.split(" ")
        for keyval in arr:
            #print(keyval)
            key, val = keyval.split(":")
            passport[key] = val.strip("\n")

    valid += isValid(passport)

print(valid)




                



