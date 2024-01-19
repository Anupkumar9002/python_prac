a=int(input("enter the value between 5 and 9 : "))
if(a<5 or a>9):
    raise ValueError("value is beyond limit")
# elif(a=="quite"):
#     print("it is fine")
print("all good")
