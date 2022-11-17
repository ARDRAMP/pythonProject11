dict={}
str1=(input("enter a string"))
for n in  str1:
    if n in dict:
        dict[n]=dict[n]+1
        print(dict)
    else:
     dict[n]=1
    print(dict)
    print("character frequency")
    for m,n in dict.items():
        print(m,n)


