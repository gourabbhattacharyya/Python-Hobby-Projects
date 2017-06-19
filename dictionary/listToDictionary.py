itemPairs = [(1,1),(1,2),(1,3),(1,4),(1,4),(1,5),(1,5),(1,6),(1,7),(1,8),(1,7),(1,9),(1,12),(1,12)]
itemCount = {}          #initialize dictionary

for i in itemPairs:         #loop over list items
    if i in itemCount:
        itemCount[i] += 1       #increase count
    else:
        itemCount[i] = 1        #add item to the dictionary

for k,v in itemCount.items():       #print dictionary items
    print(k,v)