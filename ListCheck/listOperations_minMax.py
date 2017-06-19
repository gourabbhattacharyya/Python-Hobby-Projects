import heapq

grades = [10,12,15,25,39,9,7,99,1004,500]               #initialize list

print(heapq.nlargest(3, grades))                        #get the top 3 largest values from the list. Syntax : heapq.nlargest(number of items, list to iterate through)

print(heapq.nsmallest(5, grades))


stocks = [                                              #initialize list of dictionaries

    {'ticker':'apple', 'price':109.29},
    {'ticker':'google', 'price':99.59},
    {'ticker':'fb', 'price':69},
    {'ticker':'amazon', 'price':119.7},
    {'ticker':'ebay', 'price':19.39}
]


print(heapq.nlargest(2, stocks, key = lambda stocks:stocks['price']))           #get the top 2 largest values.Syntax : heapq.nlargest(number of items, list to iterate through, keyValue)