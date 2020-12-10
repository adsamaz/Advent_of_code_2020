import math

# uniqueParents = {}

# def findBags(key, keymap):
#     if key not in keymap.keys():
#         return

#     #parents = 0
#     for tupl in keymap[key]:
#         uniqueParents[tupl[0]] = 1
#         findBags(tupl[0], keymap)
#         #parents += 1 + findBags(tupl[0], keymap)
#     return
        


# with open('7/input.txt') as f:
#     keymap = {}
#     while line := f.readline():
        
#         parent, childs = line.split('contain')
#         parentKey = "".join(parent.split(" ")[:2])

#         childArray = []
#         for child in childs.split(","):
#             childItems = child.split(" ")
#             #print(parentKey, childItems)
#             number, childKey = childItems[1], "".join(childItems[2:4])
#             if childKey in keymap.keys(): 
                
#                 keymap[childKey].append((parentKey, number))
#             else:
#                 #print(keymap)
#                 keymap[childKey] = [(parentKey, number)]
#                 #print(keymap)
    

# print(keymap)
# key = "shinygold"
# findBags(key, keymap)


#uniqueChilds = {}

def findBags(key, keymap):
    if key not in keymap.keys():
        return 1

    childs = 1
    for tupl in keymap[key]:
        #uniqueParents[tupl[0]] = 1
        #findBags(tupl[0], keymap)
        print(tupl)
        childs += tupl[1] * findBags(tupl[0], keymap)
    
    return childs
        


with open('7/input.txt') as f:
    keymap = {}
    while line := f.readline():
        
        parent, childs = line.split('contain')
        parentKey = "".join(parent.split(" ")[:2])

        childArray = []
        for child in childs.split(","):
            childItems = child.split(" ")
            #print(parentKey, childItems)
            if childItems[1] == "no":
                continue

            number, childKey = int(childItems[1]), "".join(childItems[2:4])
            if parentKey in keymap.keys(): 
                
                keymap[parentKey].append((childKey, number))
            else:
                #print(keymap)
                keymap[parentKey] = [(childKey, number)]
                #print(keymap)


print(keymap)
key = "shinygold"
childs = findBags(key, keymap) - 1
print(childs)




                



