
height = float(input())

weight = int(input())

BMI=round(weight/(height**2),2)
if (BMI<18.5):
  print(f"Your BMI is {BMI}, you are slighty underweight.")
elif (25>BMI>=18.5):
  print(f"Your BMI is {BMI}, you are have normal weight.")
elif(30>BMI>=25):
  print(f"Your BMI is {BMI}, you are slighty overweight.")
elif(35>BMI>=30):
  print(f"Your BMI is {BMI}, you are obese")
else:
  print(f"Your BMI is {BMI}, you are clinically obese")

  
