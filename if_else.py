a=int(input("enter the number : "))

if(a>0):
    print("number is positive")
elif(a==0):
    print("number is zero")
else:
    print("number is negative") 

    # or if else in one line

print("a is greater than 0") if a>0 else print("a is less than zero") if a< 0 else print("a is equal to 0")       
