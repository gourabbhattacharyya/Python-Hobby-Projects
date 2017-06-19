from collections import Counter                 #import Counter class from Collecions module

text = "ONCE upon a time there were four little Rabbits, \
and their names were— Flopsy, Mopsy, Cotton-tail,and Peter.They lived with their Mother in a sand-bank, underneath the root of a very big fir tree. NOW, my dears,  \
said old Mrs. Rabbit one morning,  you may go into the fields or down the lane, but don t go into Mr. McGregor s garden: your Father had an accident there; \
he was put in a pie by Mrs. McGregor.NOW run along, and don t get into mischief. I am going out.THEN old Mrs. Rabbit took a basket and her umbrella, to the baker s.\
She bought a loaf of brown bread and five currant buns.BUT Peter, who was very naughty, ran straight away to Mr. McGregor s garden and squeezed under the gate!FIRST \
he ate some lettuces and some French beans; and then he ate some radishes;AND then, feeling rather sick, he went to look for some parsley.BUT round the end of a cucumber frame, \
whom should he meet but Mr.McGregor!MR. McGREGOR was on his hands and knees planting out young cabbages, but he jumped up and ran after Peter, waving a rake and calling out,  \
Stop thief! PETER was most dreadfully frightened; he rushed all over the garden, for he had forgotten the way back to the gate.He lost one of his shoes among the cabbages, \
and the other shoe amongst the potatoes."


words = text.lower().split()                #split the text to words

counter = Counter(words)                    #count elements from a string

topThreeFreqWords = counter.most_common(3)          #get the top 3 elements from the text

print(topThreeFreqWords)                            #printout the top 3 elements