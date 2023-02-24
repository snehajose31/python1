x=input("enter the word")
t=x.split(" ")
l=list(t)
s=set(t)
for i in s:
    z=l.count(i)
    print("",i,"occur",z,"times")