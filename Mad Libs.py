#Seth Jones
#9/20/2019
#Mad Libs Input

user = input(enter your name: ")
group = input("enter a team name: ")
group2 = input("enter another team name: ")
word1 = input("enter an adjective: ")
word2 = input("enter a person's name: ")
word3 = input("enter a plural noun: ")
word4 = input("enter a plural noun: ")
word5 = input("enter an adjective: ")
word6 = input("enter a person's name: ")
word10 = input("enter a verb: ")
word11 = input("enter a noun: ")
word12 = input("enter a plural noun: ")


text = str.format("""War! The {} is crumbling under attacks by the
{} Sith Lord, {}. There are {} on both sides.
{} are everywhere.
In a stunning move, the {} droid leader,
{}, has swept into the {} capital
and kidnapped {}, leader of the {}.
As the {} Army attempts to {} the besieged capital
with their valuable {}, two {} lead a desperate mission
to rescue the captive {}....""",group,word1,word2,word3,word4,\
                  word5,word6,group,user,group,group2,\
                  word10,word11,word12,user)
print(text)
                  
