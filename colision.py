import threading
import random 
import time
import datetime
class moves:
    def __init__(self,n):
        self.x1=n//2
        self.y1=0
        self.x2=0
        self.y2=n//2    
        if 0==0:
            for nn in range(n):
                
                self.draw(self.x1,self.y1," ") #old pos 1
                self.draw(self.x2,self.y2," ") #old pos 2
 
                if self.report():
                     nn=n+2
                self.draw(self.x1,self.y1,"*")
                self.draw(self.x2,self.y2,"*")
                self.timers(1)
    
    def draw(self,x,y,s):
        self.locate(x,y,43,s)
    def report(self):
        self.locate(30,1,43,f"x1:{self.x1},y1:{self.y1}                       ")
        self.locate(30,2,43,f"x2:{self.x2},y2:{self.y2}                       ")
        if self.x1==self.x2 and self.y1==self.y2:
            self.locate(30,3,43,f"colision                       ")
            self.draw(self.x1,self.y2,"*")
 
            return True
        self.y1+=1
        self.x2+=1 
        return False
    def timers(self,s):
        time.sleep(s)
    def locate(self,xx,yy,c,s):
        print(f"\x1b[{yy};{xx}f\x1b[{c};30m{s}")    

        
    
print("\x1bc\x1b[43;30m")
movesn=16
t=moves(movesn)

