
class board():
  def report(self):
    for x,y in self.bot:
        print(x,y)

  def insert(self,x:int,y:int):
    xy=[x,y]
    self.bot=self.bot+[tuple(xy)]
    

class users(board):
  
  def __init__(self):
    self.bot=[]


print("\x1bc\x1b[43;30m")
aa=users()
for n in range(10):
  aa.insert(n,n)
aa=aa.report()