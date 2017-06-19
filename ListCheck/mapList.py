income = [10, 40, 95]                                       #define list

def doubleIncome(dollers):                                  #define mathod for doubling the income
    return dollers*2

newIncome = list(map(doubleIncome, income))           #map will call method mentioned in the 1st argument and passes the input element specified in 2nd argument
print(newIncome)