itemDict = {

    "Rice" : 20,
    "Chicken" : 5,
    "Vegetable" : 10,
    "Icecream" : 5,
    "Juice" : 6,
    "Fruits" : 7
}

priceList = []                      #declare new list to store the values from the dictionary

for k,v in itemDict.items():        #loop over dictionary items
        priceList.append(v)   

print(sorted(priceList))