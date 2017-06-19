class Parent:                 #parent class

    def last_Name(self):        #method in Parent class
        self.lastName = 'Bhattacharyya'


class Child(Parent):        #Child class inheriting the 'Parent' class

    def first_Name(self):           #method in Child class
        self.firstName = 'Gourab '

    
    def last_Name(self):            #method overridding in Child class that is inherited from parent class
        self.lastName = 'Shilpi Bhattacharyya'


GB = Child()            #object of Child class
GB.first_Name()
GB.last_Name()
print('My fulll name is : ' + GB.firstName + GB.lastName)