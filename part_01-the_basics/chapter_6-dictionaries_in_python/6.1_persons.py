"""
Persons program in Python - this program uses the Dictionary data
structure to store information about a person I know,
I need to store their:
    - first name
    - last name
    - age
    - city
Once this is done, I then need to ensure that I print out their details
"""
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

person_dict = {}

print('So your details are: ' + 
      'Name: ' +str(person_0['name']) +
      'Surname: '+str(person_0['surname']) +
      'Age: ' + int(person_0['age']) + 
      'City' + str(person_0['city']))

user_input = str(input("Should I add you to the Database to remember your details\n"
                "Enter 'Y' for 'yes' or 'N' for 'no': "))
print('------------------------------------------------')
user_input.upper()
if user_input == 'Y':
    for persons in person_dict:
        person_dict.append(person_0)