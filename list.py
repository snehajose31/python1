l1=[]
l2=[]
l3=[]
s=int(input("enter the size of the list"))
for i in range(s):
    ele=int(input("enter the element"))
    l1.append(ele)
print("list of element",l1)
l2=[i for i in l1 if i>0]
l3=[i for i in l1 if i<0]
print("the list of postive list",l2)
print("the element removed from the list",l3)