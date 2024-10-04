#Write to program that calculates to splits the bill ,
#calculates the tips and adds the caluclated tips in splitted bill
print("Welcome to the Tip-Calculator!!!!")
#take the amount of bill as input

bill=float(input("What was the Total Bill? "))
#Calculate the tip 
tip=float(input("How much tip would you like to give ? 10, 12 or 15 ?")) 
calc_tip=bill*(tip/100)
#How many people to split the bill
num=int(input("How many people to split the bill? "))

#Each person should pay
split=bill/num
total_bill=split+(calc_tip/num)
total=round(total_bill,2)
print(f"Each person should pay:{total}")

