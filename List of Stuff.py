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
            "Super Mario 3D World",
            "Animal Crossing: New Leaf",
            "Mario Kart 8",
            "Punch Out (Wii)",
            "Legend of Zelda: Ocarina of Time",
            "Banjo Tooie",
            "Lego Star Wars: The Complete Saga",]
if "Fortnite" in favGames:
    print("Fail")
elif "Banjo Kazooie" not in favGames:
    print("Fail")
else:
    print("Pass")
print(len(favGames))
for i in range(0 , len(favGames)):
    print(favGames[i])
for i in favGames:
    print(i)
