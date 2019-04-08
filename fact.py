def fact(number):
    if number <= 1:
        return number == 1
    else:
        return number * fact(number-1)
    print('done')    




print(fact(10))
