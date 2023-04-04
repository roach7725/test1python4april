#taking input from the user 
month=int(input("enter the month in numbers"))
day=int(input("enter the days in numbers"))
year=int(input("Enter the year in two numberical digits"))

#checking validity of input
if month<1 or  month>12 :
    print("your month  input is invalid")
elif day<1 or day>31 :
    print("your day input is invalid")
elif  year<0 or year>=100 :
    print("your year input is invalid")
#print the output 
else :
    print(f"the date is {month}/{day}/{year}")
    print("Congratulations the date you entered is correct")
    

