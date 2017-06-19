stocks = {                                                      #define stock dictionary
    'Goog' : 100.214,
    'Yahoo' : 100.21,
    'FB' : 190.23,
    'Amazon' : 99.89,
    'Apple' : 150.56
}

list1 = zip(stocks.values(), stocks.keys())                     #convert the dictionary to list of values based on dictionary values
for a, b in list1:
    print(a, b)

print(min(zip(stocks.values(), stocks.keys())))                 #get the minimum value from the list with first argument as the key
print(max(zip(stocks.values(), stocks.keys())))                 #get the maximum value from the list with first argument as the key
print(sorted(zip(stocks.values(), stocks.keys())))              #get the sorted list based on values with first argument as the key


list2 = zip(stocks.keys(), stocks.values())                     #convert the dictionary to list of values based on dictionary keys
for a, b in list2:
    print(a, b)


print(min(zip(stocks.keys(), stocks.values())))                 #get the minimum value from the list with first argument as the key
print(max(zip(stocks.keys(), stocks.values())))                 #get the maximum value from the list with first argument as the key
print(sorted(zip(stocks.keys(), stocks.values())))              #get the sorted list based on keys with first argument as the key