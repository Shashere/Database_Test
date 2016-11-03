def find_product(a,b,c):
    product=-1
    if(a==7):
        product=b*c
    elif(b==7):
        product=c
    elif(c==7):
        product=-1
    else:
        product=a*b*c

    return product

product=find_product(7,6,2)
print(product)
