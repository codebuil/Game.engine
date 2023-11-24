import threading
import random 
import time
import datetime
class player:
    def __init__(self,n):
        self.t=[]
        if n>9:
            n=9
        for nn in range(n):
            self.t=self.t+[random.randint(1,9)]
            self.locate(1,nn+1,43,"player:"+str(nn)+",")
        for mm in range(9):
            for nn in range(n):
                if mm<self.t[nn]:   
                    self.locate(mm+10,nn+1,43,str(mm))
                if mm==self.t[nn]:
                    self.locate(mm+10,nn+1,43,str(mm))
            self.timers()
        self.locate(1,n+2,43,"game over.....")
    def timers(self):
        if 0==0:
            agora = datetime.datetime.now()
            data_horas = agora.strftime("%S")
            data_hora = agora.strftime("%S")
            while(data_horas==data_hora):
                agora = datetime.datetime.now()
                data_horas = agora.strftime("%S")
    def locate(self,xx,yy,c,s):
        print(f"\x1b[{yy};{xx}f\x1b[{c};30m{s}")    

        
    
print("\x1bc\x1b[43;30m")
players=3
t=player(players)

