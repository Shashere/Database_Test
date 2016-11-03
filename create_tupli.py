import math
d=input("values :")
a=d.split(',')
q=0
list1=[]
for z in a:
      q=round(math.sqrt((50*int(z)*2)/30))
      list1.append(q)
str1=""
for i in list1:
        str1+=str(i)
str1=','.join(str1)
print(str1)
