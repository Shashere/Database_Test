sentence=input("Enter sentence :")
list1=[]
list1=sentence.split(" ")
print(list1)
list2=[]
for i in list1:
        if i not in list2:
                list2.append(i)
        
str1=" "
str2=""
str2=str1.join(list2)
print(str2)
