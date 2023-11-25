import threading
import random 
import time
import datetime
class moves:
    def __init__(self,n):
        self.z1=0
        self.z2=n//2
        
           
        if 0==0:
            for nn in range(n):
                self.board(n)
                self.drawz(self.z2,n,"2")
                self.drawz(self.z1,n,"*")
                if self.report():
                    break
                self.timers(1)
    def draw(self,x,y,s):
        self.locate(x,y,43,s)
    def drawz(self,z,nn,s):
        for n in range(nn//2-z//2,nn//2+z//2+1):
            self.locate(n,z,43,s)
    def board(self,nn):
         for n in range(nn):
             self.locate(nn//2-n//2,n,43,"z")
             self.locate(nn//2+n//2,n,43,"z")
    def report(self):
        self.locate(30,1,43,f"z1:{self.z1}                       ")
        self.locate(30,2,43,f"z2:{self.z2}                       ")
        if self.z1==self.z2:
            self.locate(30,3,43,f"colision                       ")
            return True
        self.z1+=1
        return False
    def timers(self,s):
        time.sleep(s)
    def locate(self,xx,yy,c,s):
        print(f"\x1b[{yy};{xx}f\x1b[{c};30m{s}")    

        
    
print("\x1bc\x1b[43;30m")
movesn=16
t=moves(movesn)

