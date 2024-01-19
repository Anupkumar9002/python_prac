class Employee:
    companyName="apple"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def fromStr(cls,string):
        
        return cls(string.split(",")[0],int(string.split(",")[1]))

e1=Employee("Anup",21)
print(e1.name)
string="Vivek,22"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.age)

