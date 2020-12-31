
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            tanslation = translation + letter 
    return translation


print(translate(input("enter a phrase: ")))
