# Write a program that somehow simulates a phone search in python using dictionary
# # Write a program that somehow simulates a phone search in python using dictionary
phonebook={}
phonebook={
    ######
    ######
    #####
    ######
    ######
    ######
    #For you to add
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
        print(f"The result of the number you have searched is{phonebook[search_number]}")
    else:
        print("Error!!No entry found")
else:
    print("Please enter 'name' or 'number' only")
