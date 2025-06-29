import tkinter as tk
 
"""
    This Python program is based on being able to select the value(colors)
    of an alien and based on the color of that Alien, we would then 
    assign values to the player based on whethter they selected what
    color
"""
print("Welcome to my Alien Blasters program, where we are then going to "
    +"take you, our player, into our Alien World and based on the color "
    +"of the alien you choose, you blast them and are given points "
    + "================================================================")
#Contstructing a GUI with TKinter
root = tk.Tk()

user_lives = 3
green_alien = {"Color": "Green", "Points": "3"}
yellow_alien = {"Color": "Yellow", "Points" : "5"}
red_alien = {"Color": "Red", "Points": "10"}

aliens_list = [green_alien, yellow_alien, red_alien]

user_points = 0
green_alien_points = int(green_alien["Points"])
yellow_alien_points = int(yellow_alien["Points"])
red_alien_points = int(red_alien["Points"])

for aliens in aliens_list:
    print("The " + aliens['Color'] +" aliens are chasing after you!!")

user_input = str(input("Which one do you shoot first: \n" 
    +"Enter your selection here(the Alien Color): "))
while user_input != None:
    if user_input == aliens_list[0]:
        user_points = user_points + green_alien_points
        print("Great shot, you have taken down a Green Alien and "
    +"that takes you total points to " + str(user_points))
        user_input = str(input("Oh no The Alients are getting closer: \n" 
    +"Shoot down which alien (the Alien Color): "))

    elif user_input == aliens_list[1]:
        user_points = user_points + yellow_alien_points
        print("Great shot, you have taken down a Yellow Alien and "
    +"that takes you total points to " + str(user_points))
        user_input = str(input("Oh no The Alients are getting closer: \n" 
    +"Shoot down which alien (the Alien Color): "))

    elif user_input == aliens_list[2]:
        user_points = user_points + red_alien_points
        print("Great shot, you have taken down a Red Alien and "
    +"that takes you total points to " + str(user_points))
        user_input = str(input("Oh no The Alients are getting closer: \n" 
    +"Shoot down which alien (the Alien Color): "))

    else:
        print("Oh no you've been attacked and you have lost a life point" 
        +"for not selecting the right color alien to kill")
        user_lives = user_lives - 1
        user_input = str(input(f"Your current lives are {user_lives}"
                    +"\n\nTry again and enter a valid Alien Color: "))
        if user_lives == 0:
            print("You have died.")
            break