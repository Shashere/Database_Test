#PF-Tryout
def find_armstrong(number):
    temp=0
    temp1=number
    
    while(temp1!=0):
        remainder=temp1%10
        
        temp1=temp1//10
        
        temp+=(remainder*remainder*remainder)
    print(temp)
    if(number==temp):
        return True
    return False
        
number=371
if(find_armstrong(number)):
    print(number,"is an Armstrong number")  
else:
    print(number,"is not an Armstrong number")
