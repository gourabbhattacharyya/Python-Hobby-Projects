import operator

users = [
    {'fName' : 'Bucky', 'lName' : 'Roberts'},
{'fName' : 'Tom', 'lName' : 'Roberts'},
{'fName' : 'Berney', 'lName' : 'Zunks'},
{'fName' : 'Jenna', 'lName' : 'Heys'},
{'fName' : 'Sally', 'lName' : 'Jones'},
{'fName' : 'Phebey', 'lName' : 'Buffey'},
{'fName' : 'Monica', 'lName' : 'Galler'},
{'fName' : 'Ross', 'lName' : 'Galler'},
{'fName' : 'Ross', 'lName' : 'Jaller'},
{'fName' : 'Joey', 'lName' : 'Tribiany'},
{'fName' : 'Chandler', 'lName' : 'Bing'},
]

print('-------------------------Print sorted elements based on firstName-------------------------')
for item in sorted(users, key = operator.itemgetter('fName')):                      #sort the list of dictionary items using first name
    print(item)

print('-------------------------Print sorted elements based on lastName-------------------------')
for item in sorted(users, key = operator.itemgetter('lName')):                      #sort the list of dictionary items using last name
    print(item)


print('-------------------------Print sorted elements based on firstName and lastName-------------------------')
for item in sorted(users, key = operator.itemgetter('fName', 'lName')):             #sort the list of dictionary items using first name and last name
    print(item)