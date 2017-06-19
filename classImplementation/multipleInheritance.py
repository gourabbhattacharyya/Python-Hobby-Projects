class Mario():              #class no:1

    def move(self):
        print('I am moving')


class Shroom():             #class no:2

    def eatShroom(self):
        print('I am big now!!!!')


class idle():              #class no:3 with no functionality or blank class for future use
    pass                   #string to type for blank classes


class BigMario(Mario, Shroom):          #class no:4, inheriting multiple classes : Mario and Shroom [example of multiple inheritance]

    def fire(self):
        print('I am on fire today!!!')


bm = BigMario()         #object of BigMario class

bm.move()
bm.eatShroom()
bm.fire()
bm.move()