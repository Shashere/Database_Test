#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    delivery_charge=0
    if(distance_in_kms<=3):
            delivery_charge=0
    elif(distance_in_kms>=3 and distance_in_kms<=6):
            delivery_charge=distance_in_kms*3
    else:
            delivery_charge=(distance_in_kms-3)*6 + 9
            
    if(food_type not in ["V","N"] or quantity_ordered<1 or distance_in_kms<0):
            bill_amount=-1
    elif(food_type=="N"):
            bill_amount=150*quantity_ordered+delivery_charge
    elif(food_type=="V"):
            bill_amount=120*quantityordered+delivery_charge

            
            
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
