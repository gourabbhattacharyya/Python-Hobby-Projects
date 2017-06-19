
def zipList(list1, list2):          #method definition
    names = zip(list1, list2)       #zip 2 lists which actually concat/append/merge 1st item of list1 to 1st item of list2 and so on. Finally stores the result in the resulting list

    for a, b in names:              #loop over zipped list elements
        print('Full name is : ' + a + ' ' + b)


firstNames = ['Gourab', 'Shilpi', 'Bucky']      #list1
lastNames = ['Bhattacharyya', 'Bhattacharyya', 'Roberts']       #list2

zipList(firstNames, lastNames)      #call the method