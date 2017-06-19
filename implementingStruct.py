from struct import *

#store data in bytes format
packed_data = pack('iif', 6, 7, 5.2)
print('Packed data is : ' + str(packed_data))

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))



#convert back the bytes data back to normal
originalData = unpack('iif', packed_data)

print('Original data is : ' + str(originalData))