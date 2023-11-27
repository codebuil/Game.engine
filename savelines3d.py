import random
print("\x1bc\x1b[43;30m")
print(map)
f1=open("line3d.csv","w")
for n in range(50):
    z0=random.randint(0,10)
    y0=random.randint(0,10)-5
    x0=random.randint(0,10)-5
    z1=random.randint(0,10)
    y1=random.randint(0,10)-5
    x1=random.randint(0,10)-5
    f1.write(f"{z0},{y0},{x0},{z1},{y1},{x1}")
    print(f"{z0},{y0},{x0},{z1},{y1},{x1}")
f1.close() 

