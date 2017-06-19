class Enemy:                #define class
    life = 3

    def attack(self):
        self.life -= 1    
        print('Ouch!!!')
    

    def checkLife(self):
        if self.life <= 0:
            print('I am dead!!!!!')
        else:
            print(str(self.life) + ' life remaining')



enemy1 = Enemy()            #create object of enemy class
enemy2 = Enemy()            #create object of enemy class

enemy1.attack()             #call method inside Enemy class using object 1
enemy1.attack()
enemy1.checkLife()

enemy2.attack()             #call method inside Enemy class using object 2
enemy2.checkLife()

