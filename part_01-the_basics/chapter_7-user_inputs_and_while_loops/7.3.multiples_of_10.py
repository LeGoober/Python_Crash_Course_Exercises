#!/usr/bin/env python3
""" The Multiples of Ten Program
- this Python program requests input from 
the user and then the program will report 
whether the input is a multiple of 10.

"""

prompt = "Welcome to the Multiples of 10 Program where"
prompt += " we take your input and validate "
prompt += "whether your input is a multiple of 10. "
print(prompt)
print("===========================================")

user_input = int(input("Enter your value here: "))
while user_input != None:
    if user_input % 10 == 0:
        print(f'Your answer: {user_input} is a multiple of ten.')
        break
    else:
        print(f'Your answer: {user_input} is not a multiple of ten.')
        break
    