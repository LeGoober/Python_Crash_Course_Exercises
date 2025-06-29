"""
Program 2- Dictionary of peoples favourite numbers
"""
fav_number_dict = {
    'Sarah':'14',
    'Timothy' : '23',
    'Abboth': '99'
}

print("This program displays the list of people's favourite numbers\n"
    +"Here's the current dictionary of the numbers...")
print("----------------------------------------------")

#Printing the values according to their key value
print(fav_number_dict)
print('\n')
user_input = str(input("Would you like for your number to be entered"
    +"into the dictionary of names, enter 'yes' or 'no' to confirm"
    +"]+\n Enter here: "))

if user_input.lower() == 'yes':
    while user_input == 'yes':
        user_name = str(input("Enter your name here: "))
        fav_number_dict [user_name] = int(input("Enter your number here: "))
        user_input = str(input("Would you like to enter another name into "
        +"the dictionary\nEnter your answer here('yes' or 'no'): "))
        if user_input.lower() == 'yes':
            user_name = str(input("Enter your name here: "))
            fav_number_dict [user_name] = int(input("Enter your number here: "))
        elif user_input.lower() == 'no':
            print("Goodbye")
            break

elif user_input.lower() == 'no':
    print("Goodbye")

print("\nNow the list reads as follows.....")
print(fav_number_dict)