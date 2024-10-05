print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
combined_name=name1+name2
lowername=combined_name.lower()
t=lowername.count("t")
r=lowername.count("r")
u=lowername.count("u")
e=lowername.count("e")

true=t+r+u+e

l=lowername.count("l")
o=lowername.count("o")
v=lowername.count("v")
e=lowername.count("e")
love=l+o+v+e
score=int(str(true)+str(love))
if(score<10) or (score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>40) and (score<50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
