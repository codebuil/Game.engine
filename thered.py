import threading
import random 
import time
import datetime
def game(i):
    n=random.randint(1,9)
    for m in range(n):
        print(f"player:{i},x pos={m}")
        agora = datetime.datetime.now()
        data_horas = agora.strftime("%S")
        data_hora = agora.strftime("%S")
        while(data_horas==data_hora):
            agora = datetime.datetime.now()
            data_horas = agora.strftime("%S")
    
    print(f"player:{i},is in is position")

print("\x1bc\x1b[43;30m")
players=3
t=[]
for n in range(players):
    tt=threading.Thread(target=game(n))
    tt.start()
    t=t+[tt]

for n in range(players):
    tt=t.pop()
    tt.join()