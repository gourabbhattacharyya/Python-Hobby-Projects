class Enemy:                #define class

    def __init__(self, boost):      #this is the first and default function that gets called each time an object gets created for a class
        self.energy = boost
    
    def getEnergy(self):            #custom function
        print(self.energy)


John = Enemy(10)                    #create first object
Denerys = Enemy(20)                 #create second object

John.getEnergy()                    #retrieve energy of first object
Denerys.getEnergy()                 #retrieve energy of second object