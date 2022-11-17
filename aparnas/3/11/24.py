dict={}
str=(input("enter a string"))
print(str)
str_dict=str.split(" ")
print(str_dict)
for n in str_dict:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
for m,k in dict.items():
    print(m,k)





