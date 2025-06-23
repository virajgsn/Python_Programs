class employee:
    name = "Akash"
    salary = 50000
    class phone:
        mb_no = 9767902375
        email = "sdedits1111@gmail.com"
    


obj1 = employee()                          # create object
print("name of emplyee :  ",obj1.name)     #name of emplyee :   Akash
print("salary of employee : ",obj1.salary) #salary of employee :  50000
obj2 = obj1.phone()
#print("Phone number of employee is : ",obj2.mb_no)   #Phone number of employee is :  9767902375
print("Email of employee is :",obj2.email)           #Email of employee is  sdedits1111@gmail.com
               
