#Group Project
import sys
from time import sleep
user = input("Enter your name: ")
ft = "ft."

#-----------------------------INTRO-----------------------------#

def intro():
    print("""
Loading...
""")
    sleep(2)
    print(str.format("""
Hello, {}, and welcome to the Geometry Calculator!
Please choose an option from the list below:

1: Cube Volume
2: Circle Circumference
3: Square Area and Perimeter
4: Triangle Area

5: --Exit--
""",user))

#-----------------------------CUBE----------------------------------#

def option1():
    sleep(0.5)
    print("""
--Cube Volume Calculator--
""")
    cubeLength = input("Enter your length, width, or height in feet: ")
    sleep(0.5)
    if float(cubeLength) < 0:
        print("Please use positive numbers.")
    else:
        cubeResult = float(cubeLength) **3

    cubeEquals = str.format("""
     @ + + + + + + + + + + + @
     +\\                      +\\
     + \\                     + \\
     +  \\                    +  \\
     +   \\                   +   \\
     +    @ + + + + + + + + +++ + @
     +    +                  +    + 
     +    +                  +    +
     +    +                  +    +
     +    +                  +    +
     +    +                  +    +
     +    +                  +    +
     @ + +++ + + + + + + + + @    +
      \\   +                   \\   +
       \\  +                    \\  +
        \\ +                     \\ +
         \\+                      \\+
          @ + + + + + + + + + + + @
    length/width/height: {0}
                     
    {1}, your volume is {2} {3}""",round(float(cubeLength),2),user,round(cubeResult,2),ft+"^3")

    print(cubeEquals)

#--------------------------CIRCLE------------------------#

def option2():
    sleep(0.4)
    print("""
--Circle Circumference Calculator--
""")
    circumferanceAngle = input("Enter your radius in feet: ")
    sleep(0.5)
    Pie = 3.14

    circumferanceEquals = 2.0 *Pie* float(circumferanceAngle)

    circle = str.format("""

               %%%    %%%
          %%%              %%%

      %%%                      %%%

     %%%  radius: {0}            %%%
        -------------
     %%%                         %%%

      %%%                       %%%

       %%%                     %%%

               %%%    %%%

    {1}, your circumferance is {2} {3}""",round(float(circumferanceAngle),2),user,round(circumferanceEquals,2), ft)


    print(user,"your angle is",str(round(circumferanceEquals,2)), circle)

#------------------------------SQUARE------------------------#

def option3():
    sleep(0.5)
    print("""
--Square Area and Perimeter Calculator--
""")
    type_square= input("Enter length or width in feet: ")
    sleep(0.5)
    square= float(type_square)

    perim = square*4
    area = square**2
    squareAskie = str.format("""
    NNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMW
    NWMMMMMMMMMMMMMMMMWNNWWMMMMMMMMMMMMMMWNX  length/width: {0}
    NWMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMWNX
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

    {1}, your perimeter is {2} {3}
    and your area is {4} {3}^2.
    """, round(square,2),user,round(perim,2),ft,round(area,2))
    print(squareAskie)

#---------------------------TRIANGLE------------------------#

def option4():
    sleep(0.5)
    print("""
--Triangle Area Calculator--
""")
    tri_base_type= input("Enter base in feet: ")
    tri_height_type= input("Enter height in feet: ")
    sleep(0.5)
    tri_base = float(tri_base_type)
    tri_height = float(tri_height_type)
    tri_total = tri_height*tri_base/2
    triangle = str.format("""
                     M
                    NWM
                   KKXGS
                  KKK0KNM
                 KKK000KNW
                K0KKKKKKKNW
               KKKKKK0KKKKXW
              KKK0KKK0KKKKKNW
             KKKKKKKKKKKKK0KNW
            KKK0KKKKK00KKKK0KNW   height: {0}
           0KK0000KKK00KKKKK0KXW
          KKKKKK0KKKKKKKKKK0KKKXW
         KK0KKKK00KKK00KKKK0KKKKXM
        KKKKKKKKKKKKK00KKKKKKKKK0XW
       KKKKKKKKKKKKKK00KKKKKKKK00KXM
      0KKKK0KKKK0KKKK00KKKK0KKK00KKNM
     KKKKKK0KKKKKKKKK000KK0KKKKK0KKKKM
    KK0KXKKKXKKKXXXXXXXXXXXXXXXXXXXXXNM
                 base: {1}

    {2}, your area is {3} {4}^2.""",round(tri_height,2),round(tri_base,2),user, round(tri_total,2),ft)
    print(triangle)

#-------------------------------MENU-------------------------------#
    
def option5():
    while True:
        varify = input("Are you sure you want to quit? (yes or no): ")
        if varify == "yes":
            quit()
        elif varify == "no":
            break
        else:
            print("Please answer using 'yes' or 'no'.")
        
            

while True:
    intro()
    sleep(1.5)
    choice = input("Enter your choice - 1, 2, 3, 4, or 5: ")
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
    else:
        print("That wasn't a valid option.")



