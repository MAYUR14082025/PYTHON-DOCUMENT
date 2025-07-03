a=int(input("NUMBER 1 : "))
b=int(input("NUMBER 2:  "))
c= input("ENTER FUNCTION (*,/,+,-,**):  ") 
if(c == "*"):
    print("MULTIPLICATION IS",a*b)
elif(c== "/"):
     print("DIVISION IS",a/b)
elif (c== "+"):
     print("ADDITION IS",a+b)
elif(c== "-"):
     print("SUBSTRACTION IS",a-b)
else:
     print("{a} TO THE POWER {b} IS",a**b)

