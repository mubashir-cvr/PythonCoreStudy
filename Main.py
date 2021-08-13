from MyPackage.pack1 import display as disp1
from MyPackage.pack2 import display as disp2
from MyPackage import pack1 as firstpack
import MyPackage as customPackage
import MyPackage
disp1()
disp2()
firstpack.display()
customPackage.pack2.display()
MyPackage.pack1.display()
