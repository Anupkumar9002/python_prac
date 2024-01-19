class Student:
    def __init__(self,name,occ):
        self.__name=name    #here we have made the private variable
        self.__occ=occ       #here we have made the private variable

a=Student("Anup",21)
# print(a.__name)   #throw error
print(a._Student__name)  #use thsi convention to retrieve private class variable


    
