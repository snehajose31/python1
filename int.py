lst=[]
s=int(input("enter the limit"))
for i in range(s):
    ele=int(input("enter the elememt"))
    lst.append(ele)
print(lst)
result=[]
for i in lst:
    if i>100:
        result.append('over')
    else:
        result.append(i)
print(result)
