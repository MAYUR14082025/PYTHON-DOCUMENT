import random
a=random.randint(1,100)
i=1
print("GUESS THE NUMBER BETWEEN 1 TO 100")
while(i<=5):
    b=int(input("ENTER THE NUMBER :-"))
    if(a==b):
        print("YOU WIN THE NUMBER IS ",a)
        break
    elif(b>=a-10 and b<a):
        print("YOU ARE TOO CLOSE ")
    elif(b<=a+10 and b>a):
        print(" YOU ARE TOO CLOSE ")
    else:
        print("YOU ARE TOO FAR")
    i=i+1 
else:      
    print("YOU ARE OUT OF CHANCHES THE CORRECT ANSWER IS",a)
