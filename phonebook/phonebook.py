# Write a program that somehow simulates a phone search in python using dictionary
# # Write a program that somehow simulates a phone search in python using dictionary
phonebook={}
phonebook={
    'firstname':12345,
    'lastname':12345,
    'firstname1':45678,
    'lastname1':45678,
    'firstname2':8910112,
    'lastname2':8910112,
    'firstname3':16123543,
    'lastname3':16123543,
    12345:"firstname lastname",
    45678:"firstname1 lastname1",
    8910112:"firstname2 lastname2",
    16123543:"firstname3 lastname3"
}
search=input("Please enter 'name' to search by name and 'number' to search by phone number: ")
if search=='name':
    search_name=input("Enter a name to search: ")
    if search_name in phonebook:
        print(f"The result of the name you have searched is {phonebook[search_name]} ")
    else:
        print("No entry found")
elif (search=='number'):
    search_number=int(input("Enter a number to search: "))
    if search_number in phonebook:
        print(f"The result of the number you have searched is {phonebook[search_number]}")
    else:
        print("Error!!No entry found")
else:
    print("Please enter 'name' or 'number' only")
