txt=open ('data1.txt','r')
file_lines=txt.readlines()
print("\n content with newline charater\n")
print(file_lines)

print("\n content after removing\n")
file_lines=[x.strip() for x in file_lines]
print([x.strip() for x in file_lines])
txt.close()