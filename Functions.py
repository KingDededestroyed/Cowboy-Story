def get_name():
    while True:
        name = input("What is your name? ")
        if " " in name:
            name = name.title()
            for i in range(0,9):
                if str(i) not in name:
                    continue
                else:
                    break
            print(str.format("The name you entered was {}.",name))
            break
        else:
            print("That is a really dumb name. Try again.")
            continue
        
get_name()

