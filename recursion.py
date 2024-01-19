def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*(factorial(num-1))

a=int(input("enter the number which you want to find factorial: "))
print(factorial(a))

def fibbonacci(num):
    if(num==1):
        return 0
    elif(num==2 or num==3):
        return 1
    else:
        return fibbonacci(num-1)+fibbonacci(num-2)

print(fibbonacci(a))