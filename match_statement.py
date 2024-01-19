a=int(input("enter the number : "))
match a:
    case 0 :
        print("a is zero")
    case 4:
        print("a is four") 
    case _  if a>10: 
      print("a is greater than 10") 

    case _ if a<10 :
        print("a is less than 10")
    case _ :
     print("defalt case")

