import operator

stocks = [                                                      #define stock dictionary
    ('Goog' , 100.214),
    ('Yahoo' , 100.21),
    ('FB' , 190.23),
    ('Amazon' , 99.89),
    ('Apple' , 150.56)
]

grades = [10,12,15,25,39,9,7,99,1004,500]               #initialize list

print('Sorted Stocks without sorting key : ')
print(sorted(stocks))                                           #sort the list items without using the key for sorting

print('Sorted Stocks with sorting key: ')
print(sorted(stocks, key = operator.itemgetter(1)))             #sort the list items with using the values as key for sorting

print('Sorted grades : ')
print(sorted(grades))                                           #sort the list items


print('Sorted grades in reverse order : ')
print(sorted(grades, reverse = True))                           #sort the list items in reverse order