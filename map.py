import threading
import random 
import time
import datetime
map="""
 0123456789
0 o o o    
1    o     
2          
3 o  o o   
4   o  o   
5  o  o    
6          
7o o o o   
8          
9 o o o    

"""
class moves:
    def __init__(self,n,maps):
        self.map=maps
        self.report()    
        if 0==0:
            for nn in range(n):
                t=self.ask()
                if t:
                    self.locate(20,3,43,"on spot:           ")
                else:
                    self.locate(20,3,43,"you miss:          ")
                

    def draw(self,x,y):
         self.locate(x+2,y+4,43,"#")
    def getxy(self,x,y):
        if x<0:
            x=0
        if y<0:
            y=0
        if x>9:
            x=9
        if y>9:
            y=9
        return self.map[12*(y+1)+x+1+1]   
    def ask(self):
        self.locate(20,1,43,"                        ")
        self.locate(20,1,43,"x:")
        x=int(input("?"))
        self.locate(20,1,43,"                        ")
        self.locate(20,1,43,"y:")
        y=int(input("?"))
        t=(self.getxy(x,y)=="o")
        self.draw(x,y)
        return t
    def timers(self,s):
        time.sleep(s)
    def locate(self,xx,yy,c,s):
        print(f"\x1b[{yy};{xx}f\x1b[{c};30m{s}",end="")
    def report(self):
        print(self.map)   

        
    
print("\x1bc\x1b[43;30m")

t=moves(10,map)

