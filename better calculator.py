from math import *
num1 = float(input( "choose a number : "))
opr = (input( "choose an operator : "))
num2 = float(input( "choose another number : "))


if opr == "+" :
    print (num1 + num2)
elif opr == "-" :
    print (num1 - num2)
elif opr == "/" :
    print (num1/num2)
elif opr == "*":
    print (num1*num2)
else :
    print ("invalid opr")



    
