lst=[]
l1=[]
l2=[]
s=int(input("enter the no of list"))
for i in range(s):
    a=int(input("enter the element"))
    lst.append(a)
    if( a%2 !=0):
        l1.append(a)
    else:
        l2.append(a)
print("the element in the list",lst)
print("the requered list",l1)
print("the remain element",l2)