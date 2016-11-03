import math
number=input("Enter the Number")
str1=""
for i in number:
        str1+=i
print(str1)

num=0
list2=[]
for i in str1:
        for z in i:
                num+=int(i)*(2**(int(z)))
                print(num)
