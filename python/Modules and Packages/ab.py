
print("-----------Approach-01 for a------------")
import a
ob1 = a.Animal()
ob1.display()
print("-----------Approach-01 for b------------")
import b
ob2 = b.Bird()
ob2.display()
print("-----------Approach-02 for a------------")
from a import*
obj1 = Animal()
obj1.display()
print("-----------Approach-02 for b------------")
from b import*
obj2 = Bird()
obj2.display()
print("-----------Approach-03 for a------------")
import a as aa
ob1 = aa.Animal()
ob1.display()
print("-----------Approach-03 for b------------")
import b as bb
ob2 = bb.Bird()
ob2.display()