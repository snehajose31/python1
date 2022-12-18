n=int(input("enter the number"))
print("enter the elements")
list=[]
for i in range(0,n):
    x=int(input())
    if(x%2!=0):
        list.append(x)
print(list)