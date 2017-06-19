def findPrimeNumbers(limit):
    if limit > 2:   
        count = 0
        for n in range(2, limit+1):   #loop through 2 to (limit+1) to get all the prime numbers
            if n is 2:                #for every first value
                print(2, ' is the smallest and even Prime Number')
            else:                     #for all other values
                for x in range(2, n):   #loop through 2 to particular number
                    if n%x is 0:        #check divisibility by finding the remainder
                        count += 1
                        break     
                if count is 0:          #got the Prime Number
                    print(n, 'is a Prime Number')
                else:                   #Reset the count to 0
                    count = 0               
    elif  limit is 2:
        return 2
    else:
        print('Prime number can\'t be calculated for :', limit)


print(findPrimeNumbers(2), ' is the smallest even prime number')
findPrimeNumbers(3)
findPrimeNumbers(6)
findPrimeNumbers(21)
findPrimeNumbers(1)
findPrimeNumbers(-1)