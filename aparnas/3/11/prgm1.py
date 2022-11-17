x=int(input("enter the number of string"))
print("enter the elements")
list=[]
count=0
for i in range(0,x):
    a=input()
    list.append(a)
print(list)
for i in list:
    for j in i:
      if j=='a':
        count=count+1
print(count)
