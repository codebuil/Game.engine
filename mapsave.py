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

print("\x1bc\x1b[43;30m")
print(map)
f1=open("level1.txt","w")
f1.write(map)
f1.close() 

