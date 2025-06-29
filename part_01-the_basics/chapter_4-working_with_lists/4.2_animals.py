"""
    This program requires us to think of three animals that share 
    similar characteristics, we have to srote ther names within a list 
    and use a for loop to print out the names of the animals

        ->We'll then have to modify our program to print a statement
        about each animal(i.e. a 'dog' would make a great pet)
        ->Add a line at the end of my program stating what these animals
        have in common
"""
marina_list = ["1. Sharks", "2. Pacific Tuna", "3. Penguins"]
land_crawler_list = ["1. Lions", "2. Safari Springboks", "3. Giraffes"]
below_the_surface_list = ["1. Sharks", "2. Pacific Tuna", "3. Penguins"]

print("Welcome to our Zoo where we have three primary exhibits, and they are: "
      + "\n the Marina-Sharks, Fish of the Pacific, \n the Land Crawlers- Lions, The rest of the Jungle"
      +"\n Below the Surface- Snakes, Moles, Anteaters")
print("--------------------------------------------------------")
user_input = int(input("Which of these exhibits would you like to see:\n 1.The Marina,"
                       +"\n 2.The Land Crawlers, \n 3.Below the Surface \nEnter your selection here (or choose to exit by selecting '-1'):"))
print("-------------------------------------------------------")
while( user_input != -1):
    if user_input == -1:
        print("Thank you for coming to our Zoo and we hope you have something you'd like to see next time!"
              + "\n------------------------------------------------------------")
        break
    else:
        if user_input == 1:
            print("-------------------------------------------------------")
            print("Let's take a trip underwater as you've selected to see 'The Marina'"
                + "\n\n Well the three animals that we can expect to see are:"
                +"\n 1. Sharks \t 2. Pacific Tuna \t 3. Penguins")
            print("-------------------------------------------------------")
            print("The main attributes of these animals are:")
            for animals in marina_list:
                print(animals + " primarily lives in the following climate: the "
                    + "Pacific ocean, which has a colder current thus producing more muscular fish with darker blood vessels\n")
        elif user_input == 2:
            print("-------------------------------------------------------")           
            print("Ahh, you've selected our best exhibit yet: 'The Land Crawlers'"
                    + "\n\n Well the three animals that we can expect to see are:"
                +"\n 1. Lions \t 2. Safari Springboks \t 3. Giraffes")
            print("-------------------------------------------------------")
            print("The main attributes of these animals are:")
            for animals in land_crawler_list:
                print(animals + " primarily lives in the following climate: dry grasslands, primarily located in Africa\n")
        elif user_input == 3:
            print("-------------------------------------------------------")
            print("Ohh a bit dark, I'm afraid; you've selected to see the 'Below the Surface' exhibit"
                    + "\n\n Well the three animals that we can expect to see are:"
                +"\n 1. The Black Mamba \t 2. Kenyan Aardvark \t 3. South African ground mole")
            print("-------------------------------------------------------")
            print("The main attributes of these animals are:")
            for animals in below_the_surface_list:
                print(animals + " primarily lives in the following climate: usally live in grasslands too, but occupy space underground,"
                    +" usually lay their offspring or live birth\n")
        else:
            print("Please select a proper exhibit you'd like to see...")
        user_input = int(input("Which of these exhibits would you like to see:\n 1.The Marina,"
                        +"\n 2.The Land Crawlers, \n 3.Below the Surface \nEnter your selection here (or choose to exit by selecting '-1':"))