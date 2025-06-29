"""
    So imagine an alien was just shot down in a game, and we need to
    create a variable called alien_color and assign to it a value of 
    ->Green
    ->Yellow
    ->Red
    
    After doing so we need to write a if statement that checks whether a
    alien is green, and if it is a player then earns 5 points
    ->We also then check that if it isn't green, then we give the player
    10 points
    ->We have to write one version of this program that runs the if block
    and another that runs the else block
"""
print("""Welcome to Alien Invaders, where we are going to assign to you 
    the user points based on whether you can guess which alien is worth 
    the most points and your options are: \n1.Green Alien\n2.Yellow Alien, and\n3.Red Alien""")
print("\n---------------------------------------------------------------\n"
      +"so with all that said let us take in your input and see how many "
      +"points you are assigned with your selection")
user_input = str(input("Enter your choice between Green Alien, Yellow Alien"
    +"and Red Alien\nEnter the color you've selected: "))
print("------------------------------------------------------------------")
aliens_list = ["Green Alien", "Red Alien", "Yellow Alien"]
user_points = 0
green_alien_points = 3
yellow_alien_points = 10
red_alien_points = 10
while user_input != 'y' or user_input != 'x':
    if user_input not in aliens_list:
        print("You have made an invalid selection.")
    if user_input == aliens_list[0]:
        user_total_points = user_points + green_alien_points
        print("You have selected the Green Alien and that only gets you "
        +str(green_alien_points)+ ", hope you enjoy your total rewards of "
        +str(user_total_points))
        user_input = str("Care to try again and boost your points('y' to "
        +"continue or 'n' to quit)")
    elif user_input == aliens_list[1]:
        user_total_points = user_points + yellow_alien_points
        print("Ahh you have selected the Yellow Alien, this is one "
        +"is very rare and is worth about " + str(yellow_alien_points)
        +"and your total points are: " + str(user_total_points))
        user_input = str("Care to try again and boost your points('y' to "
        +"continue or 'n' to quit)")