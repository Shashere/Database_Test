a=[]
b=[]
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    
	for i in patient_medical_speciality_list:
		a.append(count(i))
		a.append(i)
	
    print(a)    
    return speciality
    
#provide different values in the list and test your program   
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)