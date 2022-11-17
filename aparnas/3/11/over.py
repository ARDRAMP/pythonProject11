x=int(input("enter the number of list"))
print("enter the elements")
list=[]
for i in range(0,x):
    a=int(input())
    if(a>100):
        list.append("over")
    else:
        list.append(a)
print(list)

