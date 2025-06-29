"""
    The peoples program is one that requires us to use exercise 6.1's
    program  where we collect information on their
    first and last names, their age and city.

    I will make two new dictionaries representing different 
    people and store all three dictionaries in a list called
    'people'.

    As we loop through the list, I print out all the persons 
    details
"""
# 1. User login and options
print("Welcome to the Peoples Program, where we can take note of who "
      + "you are and just get to know you better")

person_list = []

print("\nCurrently they are " + str(person_list) + " persons stored in the "
      + "application. ")
print('_______________________________________________________________')
user_input = int(input('These are the current actions to perform on the'
            +' application\n'
            '1. Input your details into the People\'s Program app,\n'
            +'2.View the current People in our program\n'
            +'3. Exit the application\n'
            +'-->>Enter selection here: '))

if user_input == 1:
      name = str(input("Enter your first name: "))
      surname = str(input("Enter your last name: "))
      age = int(input("Enter your age: "))
      city = str(input("Enter the city you stay in: "))
      print('=========================================')
      person_0 = {}
      person_0['name'] = name
      person_0['surname'] = surname
      person_0['age'] = age
      person_0['city'] = city
      print(person_0)
      #Adding the person to the list
      person_list = [person_0]
      print('=========================================')

elif user_input == 2:
      print('The users that are currently within our application are: ')
      for people in person_list:
            print('*' + people)
      print('=========================================')

elif user_input == 3:
      print('Goodbye person...')
      