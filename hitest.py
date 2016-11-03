def count(str):
        a=True
        b=False
        for i in range(0,len(str)):
                if(str[i]=='.'):
                        if(str[i+1]=='x'):
                                return b
                        else:
                                return a
        return a
        
                        
        
str='abc.xyzabc.abc'
a=count(str)
print(a)
