"""
    The Restaurant Seating Python Program
    ------------------------------------------------------
    This program requires a user to enter how many people they are 
    going to have for their dinner group. If the groups is more than 8,
    the program should print a message saying that they will have to wait
    for a table. Otherwise, the program should report that their table is
    ready.
"""
print('====================================================')
print('Welcome to the Restaurant Seating Program. \n' +
      "We need to know how many people are in your dinner group.")

user_input = int(input("Enter the amount of people in your dinner group: "))
while user_input < 2:
    print("You'll need at least 2 people to make a dinner reservation.")
    user_input = int(input("Enter the amount of people in your dinner group: "))
    if user_input > 8:
        print("This number exceeds the maximum amout of diners allowed for" +
              " a dinner reservation so you'll have to wait for a table.")
        break
    elif user_input >= 2 and user_input <= 8:
        print("We may start seating your dinner group now, your table is ready.")
        break
else:
    if user_input > 8:
        print("This number exceeds the maximum amout of diners allowed for" +
              " a dinner reservation so you'll have to wait for a table.")
    elif user_input >= 2 and user_input <= 8:
        print("We may start seating your dinner group now, your table is ready.")
print('====================================================')
print("Thank you for using the Restaurant Seating Program.")    