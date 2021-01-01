try:
    x = int(input('enter number: '))
    y = int(input('enter number: '))
    if x == 0:
        raise Exception()
    z = x / y
    print(z)
except:
    print('wrong input.')