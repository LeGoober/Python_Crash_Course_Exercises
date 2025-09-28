"""
    Project Specifications - The Car Rentals Python Program
    ------------------------------------------------------
    This program takes in the users input and asks what kinds
    of rental cars they would like to rent. It then prints out
    the users input in a formatted string.
"""

cars_list = ['Fiat', 'Ford', 'Chevrolet', 'Toyota', 'Honda']
print('====================================================')
print('Welcome to the Cars Rental, \n' + 
      'that are available for rent are: ')
for car in cars_list:
    print(f'- {car}')
print('====================================================')

user_response = str(input("What kind of rental car would you like? "))

while user_response not in cars_list:
    print("Sorry, we don't have that car available.")
    user_response = str(input("What kind of rental car would you like? "))
    if user_response in cars_list:
        print(f"Let me see if I can find you a {user_response}.")
        break
else:
    print(f"Let me see if I can find you a {user_response}.")
print('====================================================')
print("Thank you for using the Cars Rental program.")