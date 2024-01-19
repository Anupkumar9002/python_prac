class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Manager(Employee):
    def __init__(self,name,post):
        Employee.__init__(self,name)
        self.post = post

    def show(self):
        Employee.show(self)
        print(f"The dance is {self.post}")

class Peon(Manager):
    def __init__(self,name,shift):
        Manager.__init__(self,name,post="worker")
        self.shift=shift

    def show(self):
        Manager.show(self)
        print(f"employee {self.shift}")

E=Peon("ram","day")
print(E.name)
print(E.shift)
E.show()

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = Dog("tommy", "Black")
# o.show_details()
# print(GoldenRetriever.mro())

