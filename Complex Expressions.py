from time import sleep

userName = input("Enter a username: ")
password = input("Enter a password: ")

realUser = "DoctorShoss"
realPass = "win4science"

if (realUser == userName) and\
   (password == realPass) and\
   (password != "win4science") or\
   (userName == "Walter") and\
   (userName != "Chester"):
    print("Welcome.")
else:
    print("Failed. Termination will be in 5 seconds.")
    sleep(1)
    print("5")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    quit()
