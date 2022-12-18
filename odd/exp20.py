n=int(input("enter the number of elements"))
a=0
b=1
sum=0
if(n>0):
    print("enter a vaild number")
else:
    for i in range(0,n):
        a=b;
        b=sum;4
        sum=a+b
        print(sum)