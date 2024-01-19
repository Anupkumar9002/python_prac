class Math:
    def __init__(self,name):
        self.name=name
        self.occ="HR"


    @staticmethod
    def sum(a,b):
        return a+b
a=Math("anup")
print(a.name)
print(a.occ)
print(a.sum(1,2))
print(Math.sum(1,2))