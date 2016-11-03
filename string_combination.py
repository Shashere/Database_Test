#PF-Assgn-34
def find_pairs_of_numbers(list1,sum):
        list2=[]
        for z in list1:
                list2.append(z)
        list2.reverse()
        list2.sort()
        string1=""
        for i in list1:
                for j in list1:
                        if((i+j)==sum):
                                if(i>j):
                                        string1+="("+str(i)+","+str(j)+")"+","
                                elif(j>i):
                                        string1+="("+str(j)+","+str(i)+")"+","
        string1.sort()
        return string1
                           
list1=[1, 2, 7, 4, 5, 6, 0, 3]
sum=6
print(find_pairs_of_numbers(list1,sum))
