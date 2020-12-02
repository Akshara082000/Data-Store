from keyvalue import Storage
import time

Obj=Storage()

##Reading a Key that do not exists

Obj.read("NoThread")
print()

##OUTPUT:NoThread Key does not exists

##Adding a key with livetime of 1 seconds

Obj.add("Livetimecheck",{"TimeLimit":"onesecond"},lifetime=1)
print()

##Adding key greater than 32 chars

Obj.add("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",{"Reason":"Error"})
print()

##Deleting and reading a key doesnt exits 

Obj.delete("z")
print()
Obj.read("z")
print()
##working code adding,reading,deleting

Obj.add("CCC",{"dept":"cse","year":"Final"})
print()
Obj.read("BBB")
print()
Obj.delete("BBB")
print()
Obj.read("BBB")

####Accessing a key whose lifetime over

Obj.read("Livetimecheck")