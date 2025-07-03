print("ENTER YOUR MARKS OF ALL SUBJECT")
a=int(input("ENTER THE MARKS OF ENGLISH OUT OF 100 :- "))
if(a>100):
    print("ENTER YOUR MARKS PROPERLY")
else:
    b=int(input("ENTER THE MARKS OF MATHS OUT OF 100 :- "))
    if(b>100):
        print("ENTER YOUR MARKS PROPERLY")
    else:
        c=int(input("ENTER THE MARKS OF PHYSICS OUT OF 100 :- "))
        if(c>100):
            print("ENTER YOUR MARKS PROPERLY")
        else:
            d=int(input("ENTER THE MARKS OF CHEMISTRY OUT OF 100 :-"))
            if(d>100):
                print("ENTER YOUR MARKS PROPERLY")
            else:
                e=int(input("ENTER THE MARKS OF INFORMATIO TECHNONLOGY OUT OF 100 :-"))
                if(e>100):
                 print("ENTER YOUR MARKS PROPERLY")
                else:
                    print("TO GENERATE THE REPORT CARD PRESS 1 ")
                    m=int(input("ENTER :-"))
                    if(m==1):
                     sum=a+b+c+d+e
                     percent=(sum/500)*100
                     print("******REPORT CARD******")
                     print("YOUR TOTAL SCORE IS:-",sum)
                     print("YOUR PERCENTAGE IS :-",percent,"%")
                     if(sum>=300):
                        print("YOU ACHIEVED FIRST DIVISION")
                     elif(sum<300 and sum>=175):
                        print("YOU ACHIEVED SECOND GRADE")
                     else:
                        print("YOU ARE FAIL")
                    else:
                     print("YOUR REPORT CARD IS NOT GENERATED TO GENERATE IT SEEM YOU MAY DONE SOME MISTAKE")
                
                                     
        