str1=""
list1=[]
list2=[]
list3=[]
for i in range(1000,1051):
        list1.append(str(i))
for i in list1:
        for z in range(0,len(i)):
                if(i[z] not in [0,2,4,6,8]):
                        list2.append(i)
                else:
                        print(i)
                        list3.append(i)

print(list3)
                
               
