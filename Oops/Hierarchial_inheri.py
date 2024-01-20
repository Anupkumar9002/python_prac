class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Manager(Employee):
    def __init__(self,post):
        Employee.__init__(self,name="vivek")
        self.post = post

    def show(self):
        Employee.show(self)
        print(f"The post of {self.name} is {self.post}")

class PromptEng(Employee):
    def __init__(self,name,shift):
      Employee.__init__(self,name)
      self.name=name
      self.shift=shift

    def show(self):
      Employee.show(self)
      print(f"the name {self.name} do shift {self.shift}")

class webDev(PromptEng):
   def __init__(self,salary):
      PromptEng.__init__(self,name="Anup",shift="night")
      self.salary=salary 

   def show(self):
      PromptEng.show(self)
      print(f"the salary is {self.salary}")

class HR(webDev,PromptEng):
   def __init__(self,name,shift,bonus):
      PromptEng.__init__(self,name,shift)
      self.bonus=bonus

   def show_(self):
      PromptEng.show(self)
      print(f"{self.name},{self.shift},{self.bonus}")


E1=webDev("500000")
E1.show()
E2=HR("rahul","dayTime","20000")
E2.show_()
      
      
      
     