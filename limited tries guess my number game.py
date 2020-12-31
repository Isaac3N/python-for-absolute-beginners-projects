# welcome to the guess my number game
# your to guess a number from 1-5
# your limited to 3 tries

import random

print (" welcome to the guess my number game \n your limited to a number tries before the game ends \n GOOD LUCK !")

the_number = random.randint(1,5)
guess = input (" take a guess: ")
tries = 1
while guess != the_number and tries <= 3:
    if guess > str(the_number) :
        print ("lower....")
    else :
        print ("higher....")
    guess = input (" take a guess: ")
    tries += 1

print ( " congratulations! you guessed it ")
print (" and you did it in only",tries, " tries" )
    

