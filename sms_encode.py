#PF-Assgn-50

def sms_encoding(data):
        data.lower()
        list1=[]
        list1=data.split()
        print(list1)
        str1=""
        vowel=['a','e','i','o','u']
        c=0
        for i in list1:
                if i not in vowel:
                        for z in i:
                                if z not in vowel:
                                        str1+=str(z)
                        str1+=" "
                else:
                                        c+=1
                if(c==len(i)):
                        str1+=str(i)+" "
		
		
        return str1	
			
		
data="I will not repeat mistakes"
print(sms_encoding(data))
