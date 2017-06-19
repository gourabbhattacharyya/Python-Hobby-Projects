import threading            #import threading module

class GourabMessenger(threading.Thread):        #inherit Thread class in custom class

    def run(self):                  #define run method of current Thread
        for _ in range(10):
            print(threading.currentThread().getName())          #get the current thread name

a = GourabMessenger(name = 'Send out Messeges')                 #define first object with name attribute
b = GourabMessenger(name = 'Received Messeges')                 #define second object with name attribute

a.start()               #call the start() method of thread which will internally invoke run() method of object a
b.start()               #call the start() method of thread which will internally invoke run() method of object b
