import random
print("\x1bc\x1b[43;30m")

f1=open("line3d.csv","r")
map=f1.read()
f1.close() 
m=map.split("\n")
print([(-1,2,3)])
ll=[]
for n in m:
    t=tuple(())
    nn=n.split(",")
    
    t=[]
    for nnn in nn:
        

        try:
            k=int(nnn.strip())
            
            t=t+[k]
        except:
            break
        
    
    ll=ll+[tuple(t)]
print(ll)    

