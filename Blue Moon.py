#Seth Jones
#Period 1/2
#10/03/2019

#-----------------------Input Variables------------------------#

blueMoon = input("Is there a blue moon tonight? (yes or no): ")
weekDay = input("What is the day of the week? (Monday, Tuesday, etc.): ")
monthDay = int(input("What is the day of the month? (1-31): "))

play = "Playing song: --- "

#-----------------------Conditionals----------------------------#

if blueMoon == "yes" or blueMoon == "Yes":
    print(play + "Once in a Blue Moon")
elif monthDay <= 7:
    if weekDay == "Monday":
        print(play + "Manic Monday")
    elif weekDay == "Tuesday":
        print(play + "Tuesday's Gone")
    elif weekDay == "Wednesday":
        print(play + "Just Wednesday")
    elif weekDay == "Thursday":
        print(play + "Sweet Thursday")
    elif weekDay == "Friday":
        print(play + "Friday I'm in Love")
    elif weekDay == "Saturday":
        print(play + "Saturday in the Park")
    elif weekDay == "Sunday":
        print(play + "Lazing on a Sunday Afternoon")
    else:
        print(play + "Days of the Week")
else:
    print(play + "Day Dream Believer")
