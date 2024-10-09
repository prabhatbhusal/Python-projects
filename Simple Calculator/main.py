#Calculator App using Python
from art import logo

print(logo)


#Add
def add(num1,num2):
  return num1+num2
#subtract
def subtract(num1,num2):
  return num1-num2
#multiply
def multiply(num1,num2):
  return num1*num2
#divide
def divide(num1,num2):
  return num1+ num2
def calculator():
  n1=int(input("What is the first number? "))
  operations={
  '+':add,'-':subtract,'*':multiply,'/':divide
}
  should_continue=True
  while should_continue:
    for symbol in operations:
      print(symbol)
    operation_symbol=input("Pick an operation from the line above: ")
    n2=int(input("What is the next number? "))
    calculation=operations[operation_symbol]
    answer=calculation(n1,n2)
    print(f"{n1}+{n2}={answer}")
    decide=input(f"type y for continue calculating {answer} or n for exit: ")
    if decide=='y':
      n1=answer
      
    else:
      should_continue=False
      calculator()
  
