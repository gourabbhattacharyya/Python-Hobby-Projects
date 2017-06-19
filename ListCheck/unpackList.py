item = ['May 18, 2017', 'Cake', 5.98]       #define list of items
print('Date : ' + item[0] + ' Name : ' + item[1] + ' Price : ' + str(item[2]))      #access the items in the list using their position index



Date, Name, Price = ['May 18, 2017', 'Cake', 5.98]      #define list of items along with each definite element name while declaring
print('Date : ' + Date + ' Name : ' + Name + ' Price : ' + str(Price))      #access using them


def getMiddleAgv(gradesList):                   #This is the advanced method of unpacking the list items
    first, *middle, last = gradesList           #set the elements to definite item names. '*' defines any number of items that comes in that position
    avg = sum(middle)/len(middle)               #access and manipulate the items
    print('Average grade is : ' + str(avg))     #print the value


getMiddleAgv([55, 65, 40])                      #call with 1 items for each position
getMiddleAgv([55, 65, 75, 85, 40])              #call with 3 items in the middle position
getMiddleAgv([55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 40])        #call with more items in the middle position