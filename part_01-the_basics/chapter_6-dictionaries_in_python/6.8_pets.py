"""
The Pets application is one that utilizes various dictionaries and each
of them are the names of a pet with all the necessary details (i.e. the 
kind of animal, the pet owner). We then store all these in a 'Pets' 
dictionary.
 - I then loop through the entire list of pets and print each pets details
"""
Trevor = {
    'pet_type': 'south_american_boa',
    'pet_owners_name': 'Alonso Belafonte',
    'pet_birth_date': '18 Jun 16'
}

Fergie = {
    'pet_type': 'german_shepard',
    'pet_owners_name': 'Alonso Belafonte',
    'pet_birth_date': '11 Mar 21'
}

Nutmeg = {
    'pet_type': 'indonesian_gecko',
    'pet_owners_name': 'Genevieve Laudemeir',
    'pet_birth_date': '4 Aug 22'
}
# Creating the pet list
pet_list = [Trevor, Fergie, Nutmeg]

user_1_list = []
user_2_list = []
user_3_list = []
user_4_list = []


#System logins for Users
user_credentials = {
    'user_1' :{
        'first_name': '',
        'last_name': '',
        'email': '',
        'user_password': '',
        'user_role':'user'
    },
    'user_2':{
        'first_name' : '',
        'last_name': '',
        'email': '',
        'user_password': '',
        'user_role':'admin'
    }

}


print('Welcome to the South Lancaster vetenerian, select the user type '+
      'to gain access to the system, enter selection below:\n' +
      '-------------------------------------------------------\n')
user_input = int(input('1. User Signup\n'+
                       '2. Admin Login\n'+
                       '3. User Login\n' +
                       'Enter selection: '))

user_option_toggle = 0

if user_input == 1:
    print( '-------------------------------------------------------\n'+
          'Welcome to the South Lancaster vetenerian for all your pet health '+
          "needs, you have User access to the system\n")   
    user_firstname = str(input('Enter your first name: '))
    user_lastname = str(input('Enter your last name: '))
    user_email = str(input('Enter your email: '))
    user_password = str(input('Enter your password: '))
    user_role = 'user'

    new_user = {
        'first_name': user_firstname,
        'last_name': user_lastname,
        'email': user_email,
        'user_password': user_password,
        'user_role': user_role
    }
    user_credentials['user_1'] = new_user
    user_1_list.append(new_user)


    print('-------------------------------------------------------\n')
    print((new_user['first_name']) + (new_user['last_name'])+ " successfully logged in")

    print(user_credentials['user_1'])
    
    print('-------------------------------------------------------\n')
    print("Take a look at all the pets that are in store here at South Lancasterr vetenerian center: \n")
    for pet in pet_list:
        print(pet)
    

elif user_input == 2:
    print('Welcome to the South Lancaster vetenerian for all your pet health ' +
          "needs, you have administrative access to the system\n")
    
    entered_username = input('Enter your username (e.g., user_2): ')
    entered_password = input('Enter your password: ')

    # Check if the user exists and has the admin role
    if entered_username in user_credentials:
        user_data = user_credentials[entered_username]

        if user_data['user_role'] == 'admin' and user_data['user_password'] == entered_password:
            print('-------------------------------------------------------\n')
            print(f"{user_data['first_name']} {user_data['last_name']} successfully logged in as Admin.")
        else:
            print('-------------------------------------------------------\n')
            print("Invalid password or you do not have admin privileges.")
    else:
        print('-------------------------------------------------------\n')
        print("User not found.")
elif user_input == 3:
    print('Welcome to the South Lancaster vetenerian for all your pet health ' +
          "needs, you have administrative access to the system\n")
    
    entered_username = input('Enter your username (e.g., user_2): ')
    entered_password = input('Enter your password: ')   
    
    if entered_username in user_credentials:
        user_data = user_credentials[entered_username]

        if user_data['user_role'] == 'user' and user_data['user_password'] == entered_password:
            print('-------------------------------------------------------\n')
            print(f"{user_data['first_name']} {user_data['last_name']} successfully logged in as Admin.")
        else:
            print('-------------------------------------------------------\n')
            print("Invalid password or you do not have admin privileges.")
    else:
        print('-------------------------------------------------------\n')
        print("User not found.")
        

