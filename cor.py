import threading
import random 
import time
import datetime
map="""
 0123456789
0
1
2
3
4
5
6
7
8
9"""
class moves:
    def __init__(self,n,maps):
        self.x=[]
        self.y=[]
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
        for nn in range(20):
            if x== self.x[nn] and y== self.y[nn]:
                return "o"
        return " "   
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
        self.generates(20)   
    def generates(self,n):
        for nn in range(n):
            x=random.randint(0,9)
            y=random.randint(0,9)
            self.x=self.x+[x]
            self.y=self.y+[y]
            self.locate(x+2,y+4,43,"o")
print("\x1bc\x1b[43;30m")

t=moves(10,map)

