# name="abhishek"
# for i in name :
#     print(i)

# name=["anup","supriya","ruchi","anshu"]
# for i in name:
#     print(i)    

# for i in range(5):
#     print(i+1)

# for i in range(1,10,2):   # 3rd argument is quantity by which it will iterate
#     print(i)  
# i=1
# while(i<=10):
#     print(i)
#     i=i+1      

marks=[12, 23, 34, 98, 75]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("awesome!")
    index+=1

    # another method
marks=[12, 23, 34, 98, 75]

for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("awesome!")
