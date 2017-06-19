def sum_values(*args1):         #Function with unlimited integer type arguments
    total = 0
    for a in args1:
        total += a    
    print(total)
    

sum_values(3)
sum_values(5,3,2,4)
sum_values(1,2,3,4,5,6,7,8,9,100,1000,2000,20000,5000000)




def cat_values(*args2):         #Function with unlimited string type arguments
    sum = ''
    for str in args2:
        sum += str
        sum += ' '
    print(sum)


cat_values('Gourab')
cat_values('GB','SB')