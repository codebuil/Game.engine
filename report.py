import threading
import random 
import time
import datetime
class xyz:
    def __init__(self):
        self.zxyindex=[(7,9,0,0),(3,6,4,1),(1,1,1,2)]   
        self.zxyindex.sort()
        self.report()
    def report(self):
        print("z,x,y,index")
        for n in self.zxyindex:
            i=0
            for m in n:
                print(str(m),end="")
                if(i!=len(n)-1):
                    print(",",end="")
                i+=1
            print()
    
print("\x1bc\x1b[43;30m")

t=xyz()

