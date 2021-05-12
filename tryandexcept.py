def divide42by(num):
    try: 
        return (42/num)
    except ZeroDivisionError:
        print('Error: Can not divide by zero')
    
print(divide42by(14))

cats = input('How many cats do you have?')

try: 
    if int(cats) > 3 :
        print (f"Wow you have(num_cats, Thats a lot")
    elif int(cats) <= 3 and int (cats) > 0 :
        print (f"You just have {cats} cat(s) thats pretty small, you should get more cats!")
    elif int(cats == 0): 
        print (f"I am guessing that you are a dog person, sighs")
    elif int(cats < 0): 
        print (f'I dont think its possible to have that many number of cats')

except ValueError: 
    print ('We only accept values not strings :)')