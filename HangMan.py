
import random
from time import sleep
print("Welcome to Hangman. Good luck!")
HANGMAN = (
"""

   /------.
   ()     ?
   []
   ()
   []
   ()
   []
   ()
   []
/-----------\\
""",
"""
   /------.
   ()     ?
   []     O
   ()
   []
   ()
   []
   ()
   []
/-----------\\
""",
"""
   /------.
   ()     ?
   []     O
   ()     V
   []
   ()
   []
   ()
   []
/-----------\\
""",
"""
   /------\\
   ()     ?
   []     O
   ()     V\\
   []
   ()
   []
   ()
   []
/-----------\\
""",
"""
   /------.
   ()     ?
   []     O
   ()    /V\\
   []
   ()
   []
   ()
   []
/-----------\\
""",
"""
   /------\
   ()     ?
   []     O
   ()    /V\\
   []     x
   ()
   []
   ()
   []
/-----------\
""",
"""
   /------.
   ()     ?
   []     O
   ()    /V\\
   []     x
   ()    /
   []    
   ()
   []
/-----------\\
""",
"""
   /------.
   ()     ?
   []     O
   ()    /V\\
   []     x
   ()    / \
   []
   ()
   []
/-----------\\
""")

MAX_WRONG = len(HANGMAN) -1
WORD_BANK = ["GALLOWS",
             "INCANDESCENT",
             "IRREPAIRABLE",
             "VARIABLE",
             "EVINCE",
             "PROGRAMMING",
             "PALPATINE"]

word = random.choice(WORD_BANK)
soFar = "-" * len(word)

wrong = 0
used = []

while wrong < MAX_WRONG and soFar != word:
    sleep(1)
    print(soFar)
    print(HANGMAN[wrong])
    print("\nYou've used the following letters: \n")
    sleep(0.3)
    if not used:
        print("None")
    print(used)
    sleep(0.3)
    print("\nSo far, the word is: \n", soFar)
    sleep(0.5)
    
    letter = input("\n\nEnter a letter\n: ")
    letter = letter.upper()

    while letter in used:
        print("The letter",letter,"has already been used.")
        letter = input("Enter a letter: ")
        letter = letter.upper()

    used.append(letter)
    if letter in word:
        print("You have guessed correctly.",letter,"is in the word.")
        new = ""
        for i in range(len(word)):
            if letter == word[i]:
                new += letter
            else:
                new += soFar[i]
        soFar = new
    else:
        print("\nYou have guessed incorrectly.",letter,"is not in the word.")
        wrong += 1
        
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou have failed. The man is dead.\n")
if soFar == word:
    sleep(1)
    print("\nYou are this man's saviour.\n")

print("\nThe word was",word)
input("\n\nPress the enter key to exit.")
                    
            
                  


