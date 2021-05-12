def divide42by(num):
    try: 
        return (42/num)
    except ZeroDivisionError:
        print('Error: Can not divide by zero')
    
print(divide42by(14))