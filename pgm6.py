l1=[20,30,21,51,84,21]
l2=[40,84,21,61,31,20]
print("length of list1",l1)
print("length of list1",l2)
if len(l1)==len(l2):
    print("two list are same length")
total=sum(l1)
print("sum of list1",total)
total=sum(l2)
print("sum of list 2",total)
if sum(l1)==sum(l2):
    print("two list sum ")
print("value occur in both:")
for i in l1:
    if i in l2:
        print(i)