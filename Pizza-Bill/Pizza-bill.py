print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

if (size=='S'):
    bill=15
    if(add_pepperoni=='Y'):
      bill1=bill+2
      if(extra_cheese=='Y'):
        bill2=bill1+1
        print(f"Your final bill is: ${bill2}.")
      else:
        print(f"Your final bill is: ${bill1}.")
    else:
      bill3=bill+1
      print(f"Your final bill is: ${bill3}.") 
elif(size=='M'):
    bill=20
    if(add_pepperoni=='Y'):
      bill1=bill+3
      if(extra_cheese=='Y'):
        bill2=bill1+1
        print(f"Your final bill is: ${bill2}.")
      else:
        print(f"Your final bill is: ${bill1}.")
    else:
      
      print(f"Your final bill is: ${bill3}.")
elif(size=='L'):
    bill=25
    if(add_pepperoni=='Y'):
      bill1=bill+3
      if(extra_cheese=='Y'):
        bill2=bill1+1
        print(f"Your final bill is: ${bill2}.")
      else:
        print(f"Your final bill is: ${bill1}.")
    else:
      
      print(f"Your final bill is: ${bill}.")
else:
  print("Please choose a S,M or L only")
