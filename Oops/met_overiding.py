class shape1:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    
    def rectArea(self):
        return self.x*self.y
    
class shape2(shape1):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    
    def circleArea(self):
        
        return 3.14*super().rectArea()
    
b=shape1(2,3)
print(b.rectArea())
c=shape2(5)
print(c.circleArea())