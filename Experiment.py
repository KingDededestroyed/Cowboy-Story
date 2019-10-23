#Age
from time import sleep
divideLines = "=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~="
typeIn = input("Age: ")

def correct_age():
    while True:
        try:
            age = int(typeIn)
            print("Initiating lines...")
            print(divideLines)
            break
        except ValueError:
            print("**-Please enter a valid number-**")
            quit()
            
correct_age()
age = int(typeIn)
    
#Line Headers
bar = "Bartend: "
friend = "Friend: "
mom = "Mom: "
boss = "Boss: "


#----------------------------True/False Variables------------------------------#

#Child
if age <= 13:
    isYoung = True
else:
    isYoung = False

#License
if age >= 16:
    hasLicense = True
else:
    hasLicense = False
    
#Beer
if age >= 21:
    canBuyBeer = True
else:
    canBuyBeer = False

#Job
if age >= 18:
    hasJob = True
    if age >= 65:
        retired = True
    else:
        retired = False
else:
    hasJob = False

#Middle Aged
if age >= 40:
    if retired == False:
        midAge = True
else:
    midAge = False

#Death
if age >= 96:
    isDead = True
else:
    isDead = False
if age >= 89:
    friendDead = True
else:
    friendDead = False

#College
if age >= 20 and age < 25:
    goesToCollege = True
else:
    goesToCollege = False
    
#-------------------------Character Lines-------------------------------#
    
#Death Lines

if isDead == True:
    sleep(1.5)
    print("[you are deceased]")
    print(divideLines)
if isDead == False:

#Bartender Lines
    sleep(2)
    if isYoung == True:
        print(bar + "Where are your parents?")
    if isYoung == False:
        if canBuyBeer == False:
            print(bar + "Come back when you're 21.")
        if canBuyBeer == True:
            if retired == True:
                print(bar + "That'll be six dollars, with senior discount.")
            if retired == False:
                print(bar + "That'll be eight dollars.")

    print(divideLines)

#Friend Lines
    sleep(1.5)
    if isYoung == True:
        print(friend + "Give me back my toy!")
    if friendDead == True:
        print("[your friend is deceased]")
        gotHomeLate = False
    if isYoung == False:
        if friendDead == False:
            if hasLicense == True:
                if canBuyBeer == False:
                    print(friend + "Bruh, pass the vape...")
                    gotHomeLate = True
                if canBuyBeer == True:
                    if retired == False:
                        if midAge == False:
                            print(friend + "*drunkenly flails around*")
                            gotHomeLate = True
                        if midAge == True:
                            print(friend + "How's that job working out for you?")
                            gotHomeLate = False
                    if retired == True:
                        print(friend + "Remember the good ol' days?")
                        gotHomeLate = False
            if hasLicense == False:
                print(friend + "Let's call you an Uber.")
                gotHomeLate = False

    print(divideLines)

#Mom Lines
    sleep(1.5)
    if isYoung == True:
        print(mom + "What a strapping young lad you are!")
    if isYoung == False:
        if gotHomeLate == True:
            if canBuyBeer == False:
                print(mom + "I told you to be back by 11!")
            if canBuyBeer == True:
                print(mom + "I do not support your flamboyant lifestyle.")
        if gotHomeLate == False:
            if canBuyBeer == False:
                print(mom + "I'm glad you're being safe honey.")
            if canBuyBeer == True:
                if retired == False:
                    if midAge == True:
                        print(mom + "What a nice life you've built for yourself.")
                    if midAge == False:
                        print(mom + "I'm glad you're being responsible.")
                if retired == True:
                    print("[your mother is deceased]")

    print(divideLines)

#Boss Lines
    sleep(1.5)
    if hasJob == True:
        if retired == False:
            if gotHomeLate == True:
                if goesToCollege == False:
                    print(boss + "You seem really unfocused today.")
                if goesToCollege == True:
                    print(boss + "You're fired for slacking off!")
            if gotHomeLate == False:
                print(boss + "You're doing a good job.")
        if retired == True:
            print("[you're already retired]")
    if hasJob == False:
        if isYoung == False:
            print("[you don't have a job yet]")
        if isYoung == True:
            print("[you don't need a job yet]")

    print(divideLines)
