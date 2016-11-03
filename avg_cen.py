def centered_avg(list1):
        a=max(list1)
        b=min(list1)
        list1.remove(a)
        list1.remove(b)
        sum=0
        avg=0
        leng=len(list1)
        print(list1)
        for i in list1:
                sum+=i
        avg=sum//leng
        
        return avg

list1=[-10, -4, -2, -4, -2, 0]
avg=centered_avg(list1)
print(avg)
                
