from threading import *
from time import sleep

class EvenNumbersThread(Thread):
    def run(self):
        print(current_thread().getName())   
        for i in range(1,101):
            if (i%2==0):
                print(i)
               
            
class OddNumbersThread(Thread):
    def run(self):
        sleep(1)
        print(current_thread().getName())
        for i in range(1,101):
            if (i%2!=0):
                print(i)
                i+=1
            
class MainThread(Thread):
    def run(self):
        sleep(2)
        print(current_thread().getName())
        i=1
        while(i<=100):
            print(i)
            i+=1
            
tEven= EvenNumbersThread()
tOdd= OddNumbersThread()
tMain= MainThread()
tEven.start()
tOdd.start()
tMain.start()
