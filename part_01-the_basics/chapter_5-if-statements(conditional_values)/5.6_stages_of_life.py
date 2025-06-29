"""
    The Stages of Life program- we are tasked with writing a chain
    of if-else statements that determines a person stage of life,
    so we set a value for their age as a variable and then determine 
    at what stage they are in their life
"""

print("The Stages of Life Program")
user_input = int(input("Enter your age as a number and let us determine " 
                +"at what stage you are in your life: "))
while user_input != None:
    if user_input > 0 and user_input < 2:
        print("You are currently an infant")
    elif user_input >= 2 and user_input < 4:
        print("You are currently a toddler")
    elif user_input >= 4 and user_input < 13:
        print("You are currently a kid")
    elif user_input >= 13 and user_input < 20:
        print("You are currently a teenager")
    elif user_input >= 20 and user_input < 65:
        print("You are currently a adult")
    elif user_input >= 65: 
        print("You are an elder")
    else:
        user_input = 