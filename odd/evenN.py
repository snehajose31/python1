num=[1,2,3,4,5,6,7,8]
print("number is",num)
print("after removing the even number is")
num=[x for x in num if x%2!=0]
print(num)