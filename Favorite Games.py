import random
favGames = ["The Legend of Zelda: Majora’s Mask",
            "Banjo Kazooie",
            "Hollow Knight",
            "Shovel Knight",
            "The Legend of Zelda: Breath of the Wild",
            "Super Metroid",
            "Donkey Kong Country 2: Diddy’s Kong Quest",
            "Super Smash Bros. Ultimate",
            "Super Mario World 2: Yoshi’s Island",
            "The Legend of Zelda: Twilight Princess",
            "Donkey Kong Country",
            "Minecraft",
            "The Legend of Zelda: The Wind Waker",
            "Super Mario Galaxy",
            "Super Mario 3D World",
            "Animal Crossing: New Leaf",
            "Mario Kart 8",
            "Punch Out (Wii)",
            "Legend of Zelda: Ocarina of Time",
            "Banjo Tooie",]
if "Fortnite" in favGames:
    print("Fail")
elif favGames[1] != "Banjo Kazooie":
    print("Fail")
else:
    print("Pass")
print("-----------------------------------------")
for i in favGames:
    print(i)
randomNum = random.randint(0,6)
print("-----------------------------------------")
print(favGames[randomNum])
print("-----------------------------------------")
dumbGames = ["Fortnite",
             "World of Warcraft",
             "Halo 5",
             "Mario Kart Tour"]
for i in dumbGames:
    print(i)
             
