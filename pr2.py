#declaring the  global variable
RED="red"
YELLOW="yellow"
BLUE="blue"
#taking two primary colors as user input
color1=(input("enter the first primary color in lower case:  "))
color2=(input("enter the second primary color in lower case:   "))

if color1 not in(RED,BLUE,YELLOW) :
    print("invalid color input")
elif color2 not in(RED,BLUE,YELLOW) :
    print("invalid color input  ")
elif color1== color2:
 print("both color are same , not acceptable  ")
if color1 == RED:
        if color2 == BLUE:
            print("Your color mixture is PURPLE")
        else:
            print("Your color mixture is ORANGE") 
elif color1 == BLUE:
        if color2 == RED:
            print("Your color mixture is PURPLE")
        else:
            print("Your color mixture is GREEN")
elif  color1 ==YELLOW :
         if color2 == RED:
            print("Your color mixture is ORANGE")
            print("Your color mixture is GREEN")