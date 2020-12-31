# the guess my number game
#the player tries to guess a number from 1-10 and the computer tells the player
#whether its too high too low or just right

import random
print ("\t Welcome to the guess my number game")
print (" I am thinking of a number from 1-10 ")
print ( "try to guess it ")
# set the initial values
the_number = random.randint (1,10)
guess = int(input(" Take a guess: "))
tries = 0
out_of_guesses = False
# guessing loop
while guess != the_number and not(out_of_guesses):
    if  guess > the_number:
        print (" lower.....")
    elif guess < the_number :
        print (" higher....")
    guess = int(input( "take a guess: "))
    tries += 1
else:
        out_of_guesses = True 

print ( " you guessed it! the number was",the_number)
print ( " and it only took ",tries, "tries \n")
print ( "congratulations !!!!!!!!!!!")


input ("\n\n press the enter key to exit ")
