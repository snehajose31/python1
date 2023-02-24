str=input("enter the word")
print("orginal string",str)
r=str[0]
str=str.replace(r,"$")
str=r+str[1:]
print("after replacing ",str)