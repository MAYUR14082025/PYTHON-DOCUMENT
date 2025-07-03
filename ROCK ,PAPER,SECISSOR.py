m=0
d=0
i=1
while(i<=5):
     import random
     list = ["Rock","Paper","Scissor"]
     b = ( random.choice(list))
     a = input("Entre(Rock,Paper,Scissor):   ")
     if(a == b):
      print("TIE,POINT IS NOT GIVEN TO BOTH PLAYER")
     elif(a == "Rock" and b == "Scissor"):
      print("CONGRATULATION YOU WIN")
      m=m+1
     elif(a == "Rock" and b == "Paper"):
      print("SORRY,BUT COMPUTER WINS")
      m=m+1
     elif(a == "Paper" and b == "Rock"):
      print("CONGRATULATION YOU WIN")
      d=d+1
     elif(a == "Scissor" and b == "Rock"):
      print("SORRY,BUT COMPUTER WINS")
      d=d+1
     elif(a == "Paper" and b == "Scissor"):
      print("SORRY,BUT COMPUTER WINS")
      d=d+1
     elif(a=="Scissor" and b=="Paper"):
      print("CONGRATULAION YOU WIN")
      m=m+1
     else :
      print("WRONG INPUT,PLEASE CHECK THE INPUT PROPERLY")
      break
     i=i+1
else:
  print("YOUR SCORE IS ",m,"COMPUTER SCORE IS ",d)
  if(m>d):
    print("YOU ARE THE FINAL WINNER")
  elif(m==d):
    print("THERE IS TIE BETWEEN COMPUTER AND YOU")  
  else:
    print("COMPUTER IS FINAL WINNER") 
