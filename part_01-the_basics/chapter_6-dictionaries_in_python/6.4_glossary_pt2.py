'''
This is the second rendition of the
glossary project where I clean up the
dictionary by replacing the series of 
statements that just print out the values
of the dictionary but also run through 
the keys and the values.
 - I'll also add five more Python terms 
 that I've learnt and iterate through the
 the five terms,
 - then I'll print out the values
'''
print('Welcome to the Badwiki Python' + 
      ' glossary, where we\'ll be ' +
      'discussing various terms I\'ve' +
      'learnt during the Python course.')

glossary_dict = {
      'Explicit type casting': 'Since Python is a dynamic programming ' +
      'language, the process of explicit type casting is where we declare ' + 
      ' the type of value that a variable is storing',
      'Data Structures':'The process of using certain methods of storing a '
      +'collection of data within a program',
      'Concatenation': 'The process of concatenation is where we are able to '
      +'put together values to a String',
      'Programmatic logic': 'Through the use of certain operators (like the "if -else")'
      + 'to implement decision making within our programs',
      "Key-Value Pairs":"The key-value pair is relevant to the 'Dictionary'"+
      "data structure, where we are looking at the binding of a value that"+ 
      "reference to another value"
}

print('================================')
print("Here's a ovrview of all the values that we have within our glossary")
for keys in glossary_dict.keys():
      print(keys)

print('================================')
user_input = str(input("Would you like to see any of the definitions of " +
                  "the values that we have stored within our glossary"
                  "\nEnter 'yes' or 'no' here: "))

if user_input.lower() == 'yes':
      print('================================')
      print("Choose what values you'd like to see the definition of within "
            + "the dictionary")
      user_selection = str(input("Enter selection here: "))
      if user_selection in glossary_dict.keys():
            print("The value that you have selected is: " + user_selection)
            print("The terms ddefinition is " + glossary_dict[user_selection])
      print('================================')
      user_selection = int(input("So while you're here would you either,"
                        + "1. Add a new value to the glossary, or"
                        + "2. Choose the definition of another term,"
                        +"\nEnter your selection here: "))
      if user_selection == '1':
            
elif user_input.lower() == 'no':
