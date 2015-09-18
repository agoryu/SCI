from Cell import Cell
from EmptyCell import EmptyCell
from Agent import Agent

c1 = EmptyCell(41,42)
dsp = "x:" + str(c1.getX()) + ", y:" + str(c1.getY())
print(dsp)
if c1.isAgent():
    print("skuhalala")
else:
    print("ouuh")

print("---------------------")
    
a1 = Agent(2,1,0,-1)
dsp = "x:" + str(a1.getX()) + ", y:" + str(a1.getY()) + ", pas x:" + str(a1.pasX) + ", pas y:" + str(a1.pasY)
print(dsp)
if a1.isAgent():
    print("skuhalala")
else:
    print("ouuh")
