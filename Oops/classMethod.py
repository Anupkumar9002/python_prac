class Employee:
    companyName="apple"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def changecompanyName(cls,newcompany):
        cls.companyName=newcompany

e1=Employee("Anup",21)
print(e1.name)
print(Employee.companyName)
print(e1.companyName)
e1.changecompanyName("google")
print(e1.companyName)
