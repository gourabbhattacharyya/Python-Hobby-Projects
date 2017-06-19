#Finding all multiple of 4 using break between 1 - 100

limit = 100
for n in range(limit+10):
    if n%4 is 0:
        print(n,' is a multiple of 4')
        if n is limit:
            print('Reached Limit ',n)
            break
    else:
        print(n, 'is not a multiple of 4')


#implementing 'continue'

numbersTaken = [2, 3, 5, 7, 11, 13, 17, 19]

for n in range(1, 20):
    if n in numbersTaken:
        print(n, ' is a Prime Number')
        continue
    print(n, ' is not a Prime Number')