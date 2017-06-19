def dumb_sentence(name = 'Gourab', action = 'ate', item = 'chicken'):
    print(name , action , item)

dumb_sentence()     #calling function with default arguments
dumb_sentence("Preeti","exercise","jogging")        #calling function with new arguments without keywords and maintaining variables orders
dumb_sentence(item = 'awesome', action = 'is')      #calling function with new arguments with keywords but without variable orders