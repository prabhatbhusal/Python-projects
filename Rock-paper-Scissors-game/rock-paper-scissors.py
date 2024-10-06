rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
yourchoice=int(input("What do you choose? Type 0 for Rock,1 for Paper and 2 for Scissors :"))

compchoice=random.randint(0,2)

if(yourchoice==1 and compchoice==2):
    print("You chose:",paper)
    print("Comp choose:",scissors)
    print("You lose")
elif(yourchoice==0 and compchoice==2):
    print("You chose:",rock)
    print("Comp chose:",scissors)
    print("You win")
elif(yourchoice==0 and compchoice==1):
    print("You chose:",rock)
    print("Comp chose:",paper)
    print("You lose")
elif(yourchoice==1 and compchoice==0):
    print("You chose:",paper)
    print("Comp chose:",rock)
    print("You win")
elif(yourchoice==0 and compchoice==0):
    print("You chose:",rock)
    print("Comp chose:",rock)
    print("Draw")
elif(yourchoice==1 and compchoice==1):
    print("You chose:",paper)
    print("Comp chose:",paper)
    print("Draw")
elif(yourchoice==2 and compchoice==2):
    print("You chose:",scissors)
    print("Comp chose:",scissors)
    print("Draw")
elif(yourchoice==2 and compchoice==0):
    print("You chose:",scissors)
    print("Comp chose:",rock)
    print("You lose")
elif(yourchoice==2 and compchoice==1):
    print("You chose:",scissors)
    print("Comp chose:",paper)
    print("You win")