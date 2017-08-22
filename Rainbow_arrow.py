def check(z):
    while(z!=0):
        t = int(input())
        a = str(input()).split()
        b = []
        for i in a:
            b.append(int(i))
        j = 0
        m = 0
        z=z-1
        for i in b:
            p=b.count(i)
            if(p==1):
                j=i
        m=b.index(j)
        l1=b[0:m]
        l2=b[m+1:t]
        l2.reverse()
        if(l1==l2):
            print("yes")
        else:
            print("no")

z=int(input())
check(z)















