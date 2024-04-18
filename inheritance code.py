class Box:
    def _init_(self,name,rollno):
        self.name=name
        self.rollno=rollno
class Student:
    def _init_(self,fees):
       self.fees=fees
class Box2(Box,Student):
    def _init_(self,name,rollno,fees,marks):
        self.marks=marks
        Student._init_(self,fees)
        Box._init_(self,name,rollno)
class Box3(Box2):
    def _init_(self,sem):
        self.sem=sem
        Box2._init_(self,"shiv-raj",12,23,200000)


obj=Box3("2-1")
print(obj.sem)
print(obj.name)

obj2=Box2("shiv",12,23,200000)
print(obj2.fees)
print(obj2.marks)
print(obj2.name)
print(obj2.rollno)

obj3=Box2("raj",45,67,78900)
print(obj3.name)
print(obj3.rollno)
print(obj3.marks)
print(obj3.fees)
