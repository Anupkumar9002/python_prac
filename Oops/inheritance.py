class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class programmer(Employee):
    def __init__(self,occ):
        self.occ=occ
       
    

a=Employee("anup",21)
print(a.name,a.age)
a=programmer("HR")
print(a.occ)
    