list1=[]
for i in range(1000,3001):
        s=str(i)
        if(int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0):
                list1.append(s)
print(','.join(list1))
