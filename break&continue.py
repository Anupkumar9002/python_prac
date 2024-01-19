#break state it skip the loop after fulfilling its condition

for i in range(12):
    if(i==10):
        break
    print("2*",i+1,"=",2*(i+1))
    
#continue state it skip that given iterator present in its condition
    for i in range(12):
        if(i==10):
            continue
        print("2*",i+1,"=",2*(i+1))