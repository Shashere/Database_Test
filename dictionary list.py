def dictionary(num):
        c={}
        list1=[]
        for i in range(1,num):
                        c[i]=i*i
                        list1.append(c)
                        c={}
        print(list1)
                
                        
        
num=9
dictionary(num)

