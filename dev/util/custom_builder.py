##
 # Makes creating custom entities, items, or blocks easier.
 # dev/util/custom_builder.py
 # By Mythorical
##

selectedType = ""
validTypes = [
    "Item",
    "Block",
    "Entity"
]

def typeSelector(type):
    global selectedType
    if type in validTypes:
        selectedType = type
    else:
        print("Not a valid type!")

print("Please select your type: ")
typeSelector(input("Item, Block, or Entity\n"))

if selectedType == "Item":
    print("yay")
