salary=float(input("Please enter your salary in germany"))
country=input("Enter the country you are looking to migrate to")

def convertSalary(country,salary):
    if(country=="canada"):
        final_salary=salary*1.55
        if(final_salary>64000) :
            print("You will be rich in Canada with salary of ", final_salary,"CAD" )
        else:
            print("You will be poor in Canada with salary of ", final_salary,"CAD" )

    elif(country=="us") :
        final_salary=salary*2.5
        if(final_salary>64000) :
            print("You will be rich in uk with salary of ", final_salary,"Pounds" )
        else:
            print("You will be poor in uk with salary of ", final_salary,"Pounds" )

    elif(country=="cambodia") :
        final_salary=salary*4555
        if(final_salary>5649856) :
            print("You will be rich in cambodia with salary of ", final_salary,"cambodian riel" )
        else:
            print("You will be poor in cambodia with salary of ", final_salary,"cambodian riel" ) 

    elif(country=="united kingdom") :
        final_salary=salary*1.2
        if(final_salary>56516) :
            print("You will be rich in uk with salary of ", final_salary,"USD" )
        else:
            print("You will be poor in uk with salary of ", final_salary,"USD" ) 
    else:
        print("Invalid Country")
convertSalary(country,salary)           
    

    