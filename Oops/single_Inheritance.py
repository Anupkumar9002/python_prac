class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def sound(self):
        print("bark")

class Cat(Animal):
    def __init__(self,name,breed):
        self.breed=breed
        Animal.__init__(self,name,species="dyna")
    
    def sound(self):
        print("mew mew")

kitti=Cat("pussy","mammel")
moti=Animal("as","sd")
print(kitti)
moti.sound()
kitti.sound()
