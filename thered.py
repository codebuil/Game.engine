import threading
import random 
import time

def game(i):
    n=random.randint(1,9)
    for m in range(n):
        print(f"player:{i},x pos={m}")
        time.sleep(1)
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