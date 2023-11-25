import threading
import random 
import time
import datetime
class moves:
    def __init__(self,n):
            
        if 0==0:
            for nn in range(n):
                z=self.ask()
                self.draw(z+1,16)
    
    def draw(self,nn,n):
         z=n
         nnn=n-nn
         self.locate(n//2-nnn//2,z-nn,43,"z")
         self.locate(n//2+nnn//2,z-nn,43,"z")
    def ask(self):
        self.locate(10,1,43,"                        ")
        self.locate(10,1,43,"z:")
        return int(input("?"))
        
    def timers(self,s):
        time.sleep(s)
    def locate(self,xx,yy,c,s):
        print(f"\x1b[{yy};{xx}f\x1b[{c};30m{s}",end="")    

        
    
print("\x1bc\x1b[43;30m")
movesn=17
t=moves(movesn)

