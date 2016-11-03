sentence=input(values)
num=0
for i in sentence:
        if(i in [0,1,2,3,4,5,6,7,8,9]):
                num+=1
a=len(sentence)
b=a-num
print('no of words',b)
print('no of digits',num)                
