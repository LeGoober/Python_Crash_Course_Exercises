"""
    Exercise 6.3 - This program requires me to create a glossary, 
    which functions similarly to a dictionary. Overall, the objective of 
    this program is to create a glossary that models the functionality of 
    a dictionary,
    - this glossary will store five programming terms that I've learnt 
    through the duration of this textbook. These words will be stored
    as the key-value, and their definitions will be stored as the pair.
    - print our each word and its meaning and format the output. I'll 
    configure the program to the be able to take in user input and 
    let them choose what value they want to be printed from the glossary. 
"""
glossary_storage = {"Parsing": "The process of converting data types to " +
                    "another data type, i.e. parse the String to an Int",
                    "Iteration": "This involves using programmatic logic "+ 
                    "to then be able to pass through various values being" +
                    "stored in a data structure",
                    "Data Structures" :"The storage of data used within programs",
                    "Conditional Statements":"The 'conditional statement' is used "+
                    "when we are trying to create logic within our program based on "+
                    "the parameters of the condition meeting what is required",
                    "Key-Value Pairs":"The key-value pair is relevant to the 'Dictionary'"+
                    "data structure, where we are looking at the binding of a value that"+ 
                    "reference to another value"}

print("Welcome to the Glossary Program, where we shall be looking at "+
      "various programattic terms we've learnt throughout this crash course.")
print("Here are the key-value pairs we have stored within our glossasry " +
       "so far")
print("----------------------------------------------------------------")
for key_value in glossary_storage.keys():
    print("* " + key_value)

print("----------------------------------------------------------------")
print("So, now would you like to expand further on the definition of a term " +
      "that's been stored within our glossary,")
user_input = str(input("Enter your selection here ('Yes' or 'No'): "))
if user_input.lower() == 'yes':
    user_glossary_selection = str(input("Enter the value you would like " +
                            "its full definition on here: "))
    if user_glossary_selection in glossary_storage.keys():
        print(glossary_storage[user_glossary_selection])
    else:
        print("You haven't selected a value that is being stored within the "+ 
              "glossary.")
else:
    print("Good day")