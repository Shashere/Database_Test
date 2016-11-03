#PF-Assgn-47

def encrypt_sentence(sentence):
        list1=[]
        for i in sentence:
                list1.append(i)
        vowel=['a','e','i','o','u']
        str1=""
        str2=""
        for i in range(0,len(list1)-1):
                if(list1[i]==" "):
                        z=1
                        if(z//2==0):
                                str1+=rev(i,list1)
                                z+=1
                                print('str1',str1)
                        else:
                                str2+=conso(i,list1)
                                z+=1
                                print('str2',str2)
        return (str3)

def rev(index,list1):
        list2=[]
        str2=""
        for i in range(0,index+1):
                list2.append(list1[i])
        list2.reverse()
        for i in list2:
                str2+=str(i)
        return str2

def conso(index,list1):
        list2=[]
        str2=""
        vowel=['a','e','i','o','u']
        str3=""
        for i in range(0,index+1):
                if list1[i] not in vowel:
                        str2+=str(list1[i])
                
        for i in list1:
                str3+=str(i)

        return (str3+str2)
        
                        
                

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
