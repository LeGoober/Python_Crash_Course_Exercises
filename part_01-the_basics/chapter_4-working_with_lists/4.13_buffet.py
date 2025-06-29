"""
    This python program aims to create a tuple that will store the 
    food items in a buffet, so we will create 5 basic elements to place 
    within that tuple and we will try to throw an error where we try 
    change the values within a tuple(which is impossible since its 
    immutable)
"""

print("Welcome to Ms. Hearty's All You Can Dine buffet, where even though "
      +"our menu items stay limited, their supply and demand meet the "
      +"status of delicious every time you come and dine....... "
      +"\n_________________________________________________________________\n")
buffet_tuple = ("Starches: Potato Salad n Chives, Rocket Rice,"
                " Chippies McFries", "Poultry: Crispy Fried Chicken n Gravy, "
                "Smoked Jerk Chicken, Peking Cock", "Beef: T-Bone and Love, "
                "Braise your Beef, Meaty McTomahawk", "The Sauce and "
                 "Condiments: Big Gravy boat, Ranch")
starch_tuple = ("Potato Salad n Chives", "Rocket Rice",  "Chippies McFries")
poultry_tuple = ("Crispy Fried Chicken n Gravy", "Smoked Jerk Chicken", "Peking Cock")
beef_tuple = ("T-Bone and Love", "Braise your Beef", "Meaty McTomahawk")
snc_tuple = ("Big Gravy boat", "Ranch")
user_order_list = []

print("Our Menu Consists of the Following food items:")
for food in buffet_tuple:
    print(food)
print("=================================================================")
user_input = int(input("Select what Food Items you would like to order: "
            +"\n1. Starches, \n2. Poultry, \n3. Beef, \n4. Sauces and Condiments"
            +"\nEnter selection here(or enter '-1' to complete your "
            +"order): "))
while user_input != -1:
    if user_input == 1:
        print("\nYou have chosen to order from the Starches section, which "
        +"includes:")
        print(buffet_tuple[0])
        print("=================================================================")
        print("What would you like to order from here:")
        for starch in starch_tuple:
            print(starch)
        user_input_1 = str(input("\nEnter here:"))
        user_order_list.append(user_input_1)
    elif user_input == 2:
        print("\nYou have chosen to order from the Poultry section, which "
        +"includes:")
        print(buffet_tuple[1])
        print("=================================================================")
        for poultry in poultry_tuple:
            print(poultry)
        user_input_1 = str(input("\nEnter here:"))
        user_order_list.append(user_input_1)

    elif user_input == 3:
        print("\nYou have chosen to order from the Beef section, which "
        +"includes:")
        print(buffet_tuple[2])
        print("=================================================================")
        for beef in beef_tuple:
            print(beef)
        user_input_1 = str(input("\nEnter here:"))
        user_order_list.append(user_input_1)

    elif user_input == 4:
        print("\nYou have chosen to order from the Sauces and Condiments section, "
        +"which includes:")
        print(buffet_tuple[3])
        print("=================================================================")
        for condiment in snc_tuple:
            print(condiment)
        user_input_1 = str(input("\nEnter here:"))
        user_order_list.append(user_input_1)

    else: 
        print("Invalid selection made.")
        print("=================================================================")
    user_input = int(input("Select what Food Items you would like to order: "
            +"\n1. Starches, \n2. Poultry, \n3. Beef, \n4. Sauces and Condiments"
            +"\nEnter selection here(or enter '-1' to complete your "
            +"order): "))
    
print("=================================================================")
print("Your Final Order is:")
for items in user_order_list:
    print(items)    
try:
    buffet_tuple[0] = "Granny Steaks"
except:
    print("You can't change the values of the list as the objects in a "
          +"tuple are immutable.")