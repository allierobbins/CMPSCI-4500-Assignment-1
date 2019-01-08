'''
Assignment #1 - Dice Roll
Authors: Thomas Downs & Allie Robbins
Goal: to roll a virtual dice a specified # of times w/ a specified # of faces and record the data
Websites visited: https://www.pythonforbeginners.com/
                  https://www.tutorialspoint.com/python/
    These are indexed w/ different coding and many of them were used. Too many to list all of them.
                http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
'''
#Import needed libraries
import random

#Class for dice functions
class dice:
    def roll(self, number_of_faces) :
        return random.randint(1, number_of_faces)


#Prompt for # of rolls and check for validity
def get_valid_int_input(message, lower_bound, upper_bound):
    while True:
        user_input = input(message + ": ")
        if (user_input.isdigit()) :
            if (int(user_input) >= lower_bound and int(user_input) <= upper_bound) :
                print ("That'll work.")
                return int(user_input)
            else:
                print("That was an invalid entry. Try again.")
                continue
            print("That was an invalid entry. Try again.")
            continue
        else:
            print("That was an invalid entry. Try again.")
            
    
#Declare dice
dice1 = dice()

#Open output file
file = open("hw1output.txt", "w+")

number_of_rolls = get_valid_int_input("Enter the number of times you would like to roll the die.", 1, 100000)
number_of_faces = get_valid_int_input("Enter the number of faces the die should have, between 2 and 18.", 2, 18)

totalCount = [0] * number_of_faces
        
#print the result to screen and output file w/ spacing
for rolls in range(number_of_rolls) :
    rolled = dice1.roll(number_of_faces)                                   #roll the dice
    string = (" " * rolled + str(rolled))                   #print the roll w/ correct # of spaces    
    print (string)
    file.write(string + "\n")                               #print string to file         
    totalCount[rolled - 1] += 1
    
#Show final counts to screen 
print ("\nFinal statistics: ")
X = 0
while X < len(totalCount) :
    print ("Total # of %s's rolled: %s" % (X + 1, totalCount[X]))
    X += 1

#Print final counts to output file
file.write("\nFinal statistics: \n")
X = 0
while X < len(totalCount) :
    file.write("Total # of %s's rolled: %s" % (X + 1, totalCount[X]) + "\n")
    X += 1

#Close the output file
file.close()

#Closing statement - EOF
print("\nThe program has completed.")

    
