"""This is a Python Application that stores the names
of people within, we can use user_input to capture 
those values.
"""
names_list = []

print("To add values to a list, we can prompt the user " +
      "for input, and there are three functions that we can use to add data to a list")
user_input = str(input("Please enter a name so that it can be stored(or 'x' to stop): "))
while user_input != 'x':
    names_list.append(user_input)
    print(names_list)
    user_input = str(input("Please enter a name so that it can be stored(or 'x' to stop): "))

user_input_2= str(input("Now you can enter the position(i.e. 'first', 'second') that you want to place the name so that it can be stored(or 'x' to stop): "))
while user_input_2 != 'x':
    user_input_name = str(input("Enter your name: "))
    if user_input_2 == 'first':
        names_list.insert(0, user_input_name)
        print(names_list)
        user_input_2= str(input("Now you can enter the position(i.e. 'first', 'second') that you want to place the name so that it can be stored(or 'x' to stop): "))
        user_input_name = str(input("Enter your name: "))
    elif user_input_2 == 'second':
        names_list.insert(1, user_input_name)
        print(names_list)
        user_input_2= str(input("Now you can enter the position(i.e. 'first', 'second') that you want to place the name so that it can be stored(or 'x' to stop): "))
        user_input_name = str(input("Enter your name: "))
    elif user_input_2 == 'third':
        names_list.insert(2, user_input_name)
        print(names_list)
        user_input_2= str(input("Now you can enter the position(i.e. 'first', 'second') that you want to place the name so that it can be stored(or 'x' to stop): "))
        user_input_name = str(input("Enter your name: "))
