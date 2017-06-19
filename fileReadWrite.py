import random

name = random.randrange(500, 1000)
fileName = str(name) + '.txt'

fw = open(fileName, 'w')    #open a new file with write mode

for i in range(5):
    fw.write('I am Gourab and ')    #write values in file
    fw.write('I am awasome\n')

fw.close()                          #close the file object after use

fr = open(fileName, 'r')    #open a file with read mode
myDetails = fr.read()       #read the file content
details = myDetails.split('\n')
for line in details:
    print(line)
fr.close()                  #close the file object after use
