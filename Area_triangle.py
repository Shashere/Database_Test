#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below    
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    
    if(num1>(num2+num3)):
            return failure
    if(num2>num3+num1):
            return failure
    if(num3>num2+num1):
            return failure
	
    return success
				
				

    #Use the following messages to return the result wherever necessary 
    
 
#Provide different values for the variables, num1, num2, num3 and test your program  

A=form_triangle(1,2,7)
print(A)
