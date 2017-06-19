def getDictAverage(itemDict):           #define method for printing average of item price
    priceList = []                      #declare new list to store the values from the dictionary
    for k,v in itemDict.items():        #loop over dictionary items
        priceList.append(v)             #get the price list from item dictionary

    getAverage = lambda priceList : sum(priceList)/len(priceList)       #define function using 'labmda' keyword with 'priceList' argument to calculate the average
    
    print('Calculated Average is : ' + str(getAverage(priceList)))      #call the lambda function and get the result


getDictAverage({'milk' : 5, 'vegetable' : 10, 'chicken' : 4, 'fruits' : 7})     #call get average method and pass item dictionary as argument