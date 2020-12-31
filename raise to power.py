def raise_to_power (baseNum, powNum):
    result = 1
    for i in range(powNum):
        result *= baseNum
    return result


print (raise_to_power(3,1))
    
