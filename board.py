import threading
import random 
import time
import datetime
class moves:
    def __init__(self,n):
            
        if 0==0:
            self.boards(10)
            for nn in range(n):
                x,y=self.ask()
                self.draw(x,y)
    
    def draw(self,x,y):
         self.locate(x+2,y+2,43,"O")
         
    def ask(self):
        self.locate(20,1,43,"                        ")
        self.locate(20,1,43,"x:")
        x=int(input("?"))
        self.locate(20,1,43,"                        ")
        self.locate(20,1,43,"y:")
        y=int(input("?"))
        return x,y
    def boards(self,n):
        for nn in range(n):
            self.locate(nn+2,1,43,f"{nn}")
            self.locate(1,nn+2,43,f"{nn}")
    def timers(self,s):
        time.sleep(s)
    def locate(self,xx,yy,c,s):
        print(f"\x1b[{yy};{xx}f\x1b[{c};30m{s}",end="")    

        
    
print("\x1bc\x1b[43;30m")
movesn=17
t=moves(movesn)

