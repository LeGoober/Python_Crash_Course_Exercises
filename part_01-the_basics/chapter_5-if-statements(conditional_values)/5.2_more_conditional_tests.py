"""
    The more conditional tests Python Program:
    ->This program requires us to set up more means of creating conditional
    tests in order to better understand setting up the logic of an if-else
    statement; so we are going to set up the following:
        ->Testing for equality with Strings
        ->Running Tests using the 'lower()' function,
        ->Numerical tests that involve equality and inequality, greater 
        than and less than, greater or equal to and less than or equal too;
        ->Testing using the 'and'/'or' keywords;
        ->Testing whether an item is in a list
        ->Testing whether items is not in the list
"""

print("Welcome to Mr Conditons conditonal testing site; we are wanting to "
      +"ensure that we are able to conduct various types of conditional "
      +"tests so that we can manipulate data in Python"
      +"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("So the first test we are going to run is whether the Strings we "
      +"enter from the user are 'equal'."
      +"\n\nSo for instance, my name is Mr Conditional but I want you to "
      +"spell my name incorrectly and use small letters\n")
user_input = str(input("Enter the Lowercase name here: "))

while user_input != "Mr Conditional":
    if user_input != "Mr Conditional":
        print("You have entered the wrong name as expected, now enter the right "
        +"spelling of my name in order for the program to continue on\n")
        user_input = str(input("Enter the name here: "))
    else:
        print("Now lets move on.......................\n")

print("\nThis next part we are just going to program testing using the "
      +"'lower()' function, where we can compare the value of any input "
      +"that we may receive so that we don't have to worry about matching "
      +"the case since Python is case sensitive when conducting comarisons")
print("""------------------------------------------------------------------- "
    \nWe can take the word 'Porshe' to test this condition where we can compare the differences between 'porshe' and 'Porshe' with the lower() function
\n-------------------------------------------------------------------""")

print("Is 'porshe' equal to 'Porshe'(should be true if we were ignoring the case)")
porshe = "Porshe"
print("Testing whether 'Porshe' is equal to 'porshe'\n" +porshe == "porshe")
print("\nNow we are going to then lower the case of the variable and then "
      +"we are going to test if 'Porshe' is equal to 'porshe'(as we would "
      +"consider them to be the same word)\n")
print(porshe.lower() == 'porshe')

print("So after the conditional testing of the values of 'Porshe' we can "
      +"now focus on running numerical tests that involve equality/inequality "
      +"such as testing whether one value is greater than another, so for this "
      +"as Mr Conditional I want to make this fun.............")
print("\nSo I have a certain number of apples and I want you to choose a "
      +"number and we'll have a guessing game where I test whether you have "
      +"more apples or I have more apples.......")
mr_conds_apples = {"Number of apples": 5}
user_apples = int(input("Enter the amount of apples you want and I'll tell "
    +"you if I have more or you do\nEnter number of apples here: "))

while user_apples > mr_conds_apples["Number of apples"]:
    if user_apples > mr_conds_apples["Number of apples"]:
        user_apples = int(input("Jeez soo many apples, try again"))
    else:
        print("Big womp I have 5 apples darling........")

