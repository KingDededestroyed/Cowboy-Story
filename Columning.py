#Create name variables

name1 = "Shoss"
name2 = "Charming"
name3 = "Burnings"

#Create score variables

score1 = 1820
score2 = 355
score3 = 69

#Create title stuff

print(str.format("{0:^26}","High Scores"))
print(str.format("{0:^15}{1:^10}","Name","Score"))
print("~~~~~~~~~~~~~~~~~~~~~")

#Column Formatting

print(str.format("{0:^15}{1:^10}",name1,score1))
print(str.format("{0:^15}{1:^10}",name2,score2))
print(str.format("{0:^15}{1:^10}",name3,score3))


