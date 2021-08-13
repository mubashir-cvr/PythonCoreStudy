# from MyPackage.pack1 import display as disp1
from MyPackage.pack2 import display as disp2
from MyPackage import pack1 as firstpack
import MyPackage as customPackage
import MyPackage
disp2()
firstpack.display()
customPackage.pack2.display()
MyPackage.pack1.display()


print("\n from __init__.py")
# Configured from __init__.py in package 
import MyPackage as m
m.disp1()
m.disp2()
m.display()  # function Over load 

