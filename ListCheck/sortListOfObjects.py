from operator import attrgetter             #import attribute getter class for sorting list attributes of objects

class user:

    def __init__(self, name, userID):
        self.name = name
        self.userID = userID
    

    def __repr__(self):                    #represent the class objects
        return self.name + " : " + self.userID
    

users = [
    user('Bucky','Roberts'),
user('Tom','Roberts'),
user('Berney','Zunks'),
user('Jenna','Heys'),
user('Sally','Jones'),
user('Phebey','Buffey'),
user('Monica','Galler'),
user('Ross','Jaller'),
user('Ross','Galler'),
user('Joey','Tribiany'),
user('Chandler','Bing')
]

print("---print user objects unsorted---")
for user in users:
    print(user)


print("---print sorted users using key name---")
for user in sorted(users, key = attrgetter('name')):            #sort using name attribute
    print(user)


print("---print sorted users using key userID---")              #sort using name userID
for user in sorted(users, key = attrgetter('userID')):
    print(user)

print("---print sorted users using key name and userID---")     #sort using name and userID
for user in sorted(users, key = attrgetter('name', 'userID')):
    print(user)


'''
    for key, value in sorted(wordCount.items(), key = operator.itemgetter(1)):      #loop over sorted set of dictionary items and sort using value[operator.itemgetter(1)] or key[operator.itemgetter(0)]
        print(key, value)                                                           #print the dictionary items
'''