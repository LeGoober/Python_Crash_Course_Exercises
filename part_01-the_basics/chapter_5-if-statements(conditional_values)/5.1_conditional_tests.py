"""
    This Python program revolves around setting a series of conditional
    tests where we age going to print our a statement that describes 
    each test amd the predictions for the results of each test; our code
    should look something like:
        ->car = 'subaru'
        print("Is car == 'subaru'?, I predict true")
        print(car == 'subaru')

        print("\n Is car == 'audi', I predict false")
"""

print("!!!!!!! WELCOME TO THE CAR GUESSING GAME !!!!!!!!"
      +"\nIn this program we are going to be letting you, the user "
      +"take a guess at the cars that are in a List, and we will provide "
      +"their names but it'll be up to you to determine their existence")
cars_list = ["Lamborghini", "Aston Martin", "G-Wagon"]
cars_list_hidden = ["La*****i**", "A**** *****", "*-***on"]
for hidden_cars in cars_list_hidden:
    print("The Cars name is:" + hidden_cars)
print("------------------------------------------------------------")
user_input = str(input("\nWell now its up to you as the user to guess the "
    +"one of the cars that are within the lists and you have three lives"
    +"to get this right or else its.....DEATH"
    +"\nEnter choice here: "))
user_lives = 3

while user_lives > 0:
    if user_input in cars_list:
        print("You have selected the correct vehicle that was in the list, "+ 
            user_input + ", Lets Go.")
    else:
        user_input = str(input("Sorry buddy, you only had one shot!!!!!"
        +"\n\nKidding....try again here: "))
        user_lives - 1