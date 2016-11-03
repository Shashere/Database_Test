#PF-Assgn-46

def ReverseNumber(number, partial=0):
    if number == 0:
        return partial
    ReverseNumber=number / 10+ partial * 10 + number % 10
    if(number==ReverseNumber):
            return(number)
    else:
            number+=1
            ReverseNumber(number)
            
number=12300
print(ReverseNumber(number,0))
