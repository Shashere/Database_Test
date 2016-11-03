
	
def comp(list1,list2):
	message="a palindrome"
	message1="Not a palindrome"
	for i in list1:
		for j in list2:
			if(i==j):
				return('Palindrome')
			else:
				return('Not a Palindrome')

message="doge"
list1=[]
list2=[]
for i in message:
	list1.append(i)

for j in list1:
	list2.append(j)
list2.reverse()
a=comp(list1,list2)

print(a)


