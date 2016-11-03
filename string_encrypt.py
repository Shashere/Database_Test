#PF-Assgn-47

def encrypt_sentence(sentence):
        list1=[]
        list1=sentence.split()
        print(len(list1))
        print(list1)
        str1=""
        str2=""
        str1=rev(list1[0])+" "
        for i in range(1,len(list1)):
                if(i%2==0):
                        str1+=rev(list1[i])+" "
                else:
                        str1+=conso(list1[i])+" "
        return (str1)

def rev(m1):
        str2=""
        list2=[]
        for i in m1:
                list2.append(i)
        list2.reverse()
        for i in list2:
                str2+=str(i)
        
        return str2

def conso(m2):
        list2=[]
        for i in m2:
                list2.append(i)
        str2=""
        vowel=['a','e','i','o','u']
        str3=""
        for i in list2:
                if i not in vowel:
                        str3+=str(i)
                        
                else:
                        
        return (str3+str2)
        
                        
sentence="the sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
