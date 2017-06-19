class Girl:                         #define class

    gender = 'female'               #declare class variable

    def __init__(self, name):
        self.name = name            #declare instance variable
    


r = Girl('Rachel')                  #1st object of Girl class
m = Girl('Monica')                  #2st object of Girl class

print(r.name + ' is a ' + r.gender)
print(m.name + ' is a ' + m.gender)