l1=input("Enter the color in the list separated by comma")
l2=input("Enter the color in the list separated by comma")
x=l1.split(",")
y=l2.split(",")
s1=set(x)
s2=set(y)
s3=s1-s2
x1=list(s3)
print(x1)