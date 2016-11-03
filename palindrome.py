def check_palindrome(message):
	list1=[]
	list2=[]
	for i in message:
		list1.append(i)
	list1.reverse()
	for j in list1:
		list2.append(j)
	
	
	a=set(list1).intersection(list2)
	if(a!=0):
                          print("palindrome")
                  else:
                          print("not a palindrome")
	

message="CIVIC"
check_palindrome(message)
