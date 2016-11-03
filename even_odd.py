value=input('Enter List')
s=str(value)
s1=s.split(',')
list1=[]
for i in s1:
        if(int(i)%2!=0):
                list1.append(i)
        
print(','.join(list1))
