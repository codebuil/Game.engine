import threading
import random 
import time
import datetime
class moves:
    def __init__(self,n):
            
        if 0==0:
            for nn in range(n):
                self.locate(10,1,43,"moves:x="+str(nn)+",y="+str(nn)+"            ")
                self.locate(nn+1,nn+1,43,str(nn))
                self.timers(1)
        
    def timers(self,s):
        for n in range(s):
            agora = datetime.datetime.now()
            data_horas = agora.strftime("%S")
            data_hora = agora.strftime("%S")
            while(data_horas==data_hora):
                agora = datetime.datetime.now()
                data_horas = agora.strftime("%S")
    def locate(self,xx,yy,c,s):
        print(f"\x1b[{yy};{xx}f\x1b[{c};30m{s}")    

        
    
print("\x1bc\x1b[43;30m")
movesn=16
t=moves(movesn)

