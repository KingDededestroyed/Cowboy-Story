#-----------------------------------------Hero's Inventory------------------#
import random
from time import sleep
divideLines = "=-----------------------------------------="
error       = "=*---------------------------------------*="
speed = 0
attac = 0
defen = 0

input("\nPress the enter key to continue.")
inventMax = 10
inventory = ["Broadsword",
             "Breastplate",
             "Bomb Bag",
             "Boots",
             "Shield",
             "Hookshot",
             "Spear",
             "Bow",
             "Pegasus Boots"
             ]
equiptMax = 2
equipt = []

inventRoom = inventMax - len(inventory)
if len(inventory) < inventMax:
    print(str.format("You have room for {} more items.", inventRoom))
else:
    print("Your inventory is full.")

chestSize = random.randint(1,6)
chestItems = ["Greaves",
              "5 Fire Arrows",
              "Beam Sword",
              "5 Ice Arrows",
              "Healing Potion",
              "Stamina Potion",
              "Attack Potion",
              "5 Bombs",
              "Gun"]
sleep(2)
chest = []
print("You have found a chest! It contains: ")
print(divideLines)
for i in range(chestSize):
    chest.append(random.choice(chestItems))
for i in chest:
    print(i)
print(divideLines)
sleep(2)
print("*You add the contents of the chest to your inventory.")


inventory += chest
def too_full():
    while True:
        if len(inventory) > inventMax:
            print("Your inventory is too full: ")
            print(divideLines)
            for i in inventory:
                print(i)
            print(divideLines)
            numRem = len(inventory) - inventMax
            if numRem > 1:
                remItem = input(str.format("Please choose {} items to remove: ",numRem))
            if numRem == 1:
                remItem = input(str.format("Please choose {} item to remove: ",numRem))
            if remItem in inventory:
                inventory.remove(remItem)
            else:
                sleep(1)
                print(error)
                print("----Please choose an item in your inventory----")
                print(error)
        else:
            break
too_full()
sleep(2)

print("Your inventory is now: ")
print(divideLines)
for i in inventory:
    print(i)
print(divideLines)

sleep(2)

if len(inventory) < inventMax:
    print(str.format("You now have room for {} more items.", inventRoom))
elif len(inventory) > inventMax:
    print("Your inventory is full.")
    
for item in inventory:
    
    #--------+Defense-------#
    
    if item == "Shield":
        equipt.append(item)
        inventory.remove(item)
        defen += 10
    if item == "Breastplate":
        defen += 10
        speed -= 8
    if item == "Broadsword":
        attac += 12
    if item == "Greaves":
        speed -= 5
        defen += 5
        
    #-------+Speed---------#
        
    if item == "Boots":
        speed += 12
    if item == "Hookshot":
        speed += 18
    if item == "Pegasus Boots":
        speed += 30
        
    #--------+Attack--------#
        
    if item == "5 Fire Arrows":
        attac += 15
        defen -= 5
    if item == "Beam Sword":
        attac += 13
    if item == "Gun":
        attac += 80
    if item == "5 Bombs":
        attac += 4

print(str.format("Defense: {} -- Speed: {} -- Attack: {}",defen,speed,attac))

