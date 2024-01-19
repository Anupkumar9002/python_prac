#normal function
def avg(x,y):
    return (x+y)/2

print(avg(2,3))


#lambda function

avg2=lambda a,b: (a+b)/2
print(avg2(12,12))

# def anonymus(fx,p): IS USEFULL TO USE IN MULTIPLE FNS CALL
#     return fx(p,p)+5

# print(anonymus(avg2,2))