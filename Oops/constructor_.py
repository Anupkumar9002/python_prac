class person:
    def __init__ (self,name,occ):
        print("hello")
        self.name=name
        self.occ=occ
        self.age=18

    def info(self):
        print(f"{self.name} having age {self.age} is a {self.occ}")

a=person("harry","hr")
b=person("supu","nurse")
a.info()
b.info()