import threading
import random 
import time
import datetime
class player:
    def __init__(self,n):
        self.t=[]
        for nn in range(n):
            self.t=self.t+[random.randint(1,9)]
        for mm in range(9):
            for nn in range(n):
                if mm<self.t[nn]:   
                    print(f"player:{nn},x pos={mm}")
                if mm==self.t[nn]:
                    print(f"player:{nn},is in is position")
            self.timers()
    def timers(self):
        if 0==0:
            agora = datetime.datetime.now()
            data_horas = agora.strftime("%S")
            data_hora = agora.strftime("%S")
            while(data_horas==data_hora):
                agora = datetime.datetime.now()
                data_horas = agora.strftime("%S")
    
        
    
print("\x1bc\x1b[43;30m")
players=3
t=player(players)

