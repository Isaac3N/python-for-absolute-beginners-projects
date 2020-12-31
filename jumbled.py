# word jumble
#
# the computer picks a word and then jumbles
# then your to guess the jumbled word

import random
# a sequence of to choose from
WORD = ("difficult" , "computer" , "python" , "programming")

word = random.choice(WORD)
jumble = ""

while word :
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print ("welcome to word jumble")
print ("the jumbled word is ", word)


guess = input("\nYour guess: ")

while guess != word and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
if guess == word:
    print("That's it! You guessed it!\n")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
