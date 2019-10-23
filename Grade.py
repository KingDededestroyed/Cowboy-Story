typeGrade = input("Enter your grade: ")
myGrade = int(typeGrade)
myLetterGrade = "Not Assigned"

if myGrade >= 90:        # myGrade is greater than or equal to 90
   myLetterGrade = "A"
elif myGrade >= 80 and myGrade <=89:      # myGrade is greater than or equal to 80
   myLetterGrade = "B"
   
#add more elif and else statements here to handle C, D and F
   
elif myGrade >= 70 and myGrade <= 79:
    myLetterGrade = "C"
elif myGrade >= 60 and myGrade <= 69:
    myLetterGrade = "D"
elif myGrade <= 59:
    myLetterGrade = "F"

#print out the grade
    
print("My grade is:", myLetterGrade)
