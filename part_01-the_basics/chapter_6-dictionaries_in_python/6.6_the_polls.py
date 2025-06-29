"""The Polling Program
 - This Python application focuses on the use of the code within the 
 favourite programming list, where we have to create a list of people 
 who should take the favourite programming languages poll,
 - I need to have preconfigured names in the list and some that aren't
 
 __WHAT TO PROGRAM__
 - then I have to iterate through the list of people who should take the 
 poll, and print a message and thanking them for responding. 
 - If they haven't taken the poll, invite them to take the poll
"""
#The Favourite Programming Language dictionary
favourite_languages_dict = {
    'Ethan' : 'Rust',
    'Vuyo': 'Java',
    'Karabo': 'Java',
    'Nelson': 'C++',
    'Aiden': 'JavaScript',
    'Cheslyn' : 'Python',
    'Jane': 'Python',
    'Elvis': 'Rust',
    'Bertrom': 'C',
    'Sahmet': 'Java'
}

print("Welcome to the Programmers Polls application, where we invite you "+
      "to take part in listing your favourite language on this poll\n")
print('======================================')
user_vote = int(input("So what would you like to do today? Choose a number "
                +"to perform an operation: \n"
                + "1. View all the current participants,\n"
                + "2. View all the top languages for the favourite programming "
                + "languages, \n"
                + "3. Place your vote on your favourite programming language\n"
                + "Enter your selection here: "))
print('======================================')
if user_vote == 1:
    print("This is the current list of voters")
    for users in favourite_languages_dict.keys():
        print("* " + users)