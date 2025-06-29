#The Voting Log In application
voter_passwords = ["Amy123", "DennisR"]
vote_candidates = ["Kent Pierce", "Dean Dundee", "Kathstone Meras"]

print("Welcome to our Voting System, please enter your name and password below to login,\n")
user_name = str(input("Enter Name Here: "))
user_password = str(input("Enter Password Here: "))

if user_password in voter_passwords:
	print(user_name + " has logged in successfully! \n")
	print("Would you like to vote (enter 'yes' to vote or'exit' to quit the application)")
	user_input = str(input("\nEnter Selection here: "))
	while(user_input != None):
		if user_input == 'exit':
			break
		elif user_input == 'yes':
			for candidates in vote_candidates:
				print(candidates + " is a running candidate,")
			print("\nNow select the Candidate You'd Like to Vote for")
			user_vote = str(input("Enter Vote here: "))
			if user_vote not in vote_candidates:
				print(f"The Candidate {user_vote} is not in the Ballot")
				user_input = str(input("Would you like to vote (enter 'yes' to vote or'exit' to quit the application): "))				
			else:
				print(f"Your Vote has been captured successfully")
				user_input = str(input("Would you like to vote (enter 'yes' to vote or'exit' to quit the application): "))

else:
	print("You have either been banned from using our platform, Please enter the correct log in details.")
	