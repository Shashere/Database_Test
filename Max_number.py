#PF-Assgn-28
list1=[]
def find_max(num1, num2):
   max=-1
   list1=[]
   z=0
   for i in range(num1,num2+1):
		if(i%15==0):
			print(i)
			list1.append(i)
			z=max(list1)
			max=z
	
   return max
		
			
			
#Provide different values for num1 and num2 and test your program.
max=find_max(10,15)
print(max)