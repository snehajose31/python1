list=[]
l=int(input("enter the limit="))
for i in range(l):
    x=int(input("enter the value="))
    list.append('over' if x>100 else x)
    print(list)