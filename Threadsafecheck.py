from keyvalue import Storage
from threading import Thread
import time



Obj=Storage()

print("Thread performing all three CRD functions")


t1=Thread(target=Obj.add,args=("Placement",{"company":"Freshworks"},))
t2=Thread(target=Obj.read,args=("Fresh",))
t3=Thread(target=Obj.delete,args=("SASTRA",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
Obj.display()


print()
print("Three Threads performing Create functions")

time.sleep(3)


print()
t1=Thread(target=Obj.add,args=("T7",{"Operation":"add"},))
t2=Thread(target=Obj.add,args=("T8",{"Operation":"add"},))
t3=Thread(target=Obj.add,args=("T9",{"Operation":"add"},))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
Obj.display()

print("Three Threads performing all read functions")
print()

time.sleep(3)

t1=Thread(target=Obj.read,args=("T4",))
t2=Thread(target=Obj.read,args=("T5",))
t3=Thread(target=Obj.read,args=("T6",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
Obj.display()

print("Thread performing all three delete functions")
print()

time.sleep(3)

t1=Thread(target=Obj.delete,args=("T4",))
t2=Thread(target=Obj.delete,args=("T5",))
t3=Thread(target=Obj.delete,args=("T6",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
Obj.display()