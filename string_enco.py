
message="AABCCA"
list1=[]
for i in message:
	list1.append(i)

count1=0
list3=list(set(list1))
list2=[]
for i in list3:
	
	count1=list1.count(i)
	list2.append(count1)
	list2.append(i)

message = ''.join(str(e) for e in list2)
print(message)
