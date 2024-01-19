l=[1,2,4,5,6]
def square(x):
    return x*x

newl=[]
# for i in l:      1st method
#     newl.append(square(i))

# print(newl)

#2nd method

newl=list(map(square,l))
print(newl)

def myfns(a):
    return a>4

newnewl=list(filter(myfns,newl))
print(newnewl)

from functools import reduce 

def sum(x,y):
    return x+y
sum=reduce(sum,newl) 
print(sum)