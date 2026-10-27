def fizzbuzz(n = 100):
    result = []
    for i in range(1, n +1):
        if i % 15 == 0:
            result.append("fizzbuzz")
        elif i % 5 == 0:
            result.append("fizz")
        elif i % 3 == 0:
            result.append("buzz")
        else:
            result.append(i) 
    return result

print(fizzbuzz())

'''statement = "werg78"
if statement.isalpha():
    print("the statement has no numbers")
else:
    print("the statement has numbers")
    '''