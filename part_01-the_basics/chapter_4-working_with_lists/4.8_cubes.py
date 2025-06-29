"""
    Welcome to the Cubes python program where we are going to create 
    a list that contains the first ten numbers and cube them(raise the 
    number to the third power and use a for loop to print out the values)
"""
print("Welcome to the Cubes program where you can choose to print out a "
      +"list that will raise the numbers 1-10 to the second or third power")
print("---------------------------------------------------------")
user_value = int(input("We will create a list that stores the  these ten values and use "
      +"a for loop to then print out its values;\n"
      +"Enter 1 or 2 here whether you would like to see a list of numbers "
      +"raised to the second or third power((1) for second, (2) for third): "))

second_power_list = []
third_power_list = []
for values in range(1, 11):
    values_squared = values**2
    second_power_list.append(values_squared)
for values in range(1, 11):
    values_cubed = values**3
    third_power_list.append(values_cubed)

if user_value == 1:
    print("Here are the contents of the values in the list raised to the "
          + "second power: ")
    print(second_power_list)
elif user_value == 2:
    print("Here are the contents of the values in the list raised to the "
          + "third power: ")
    print(third_power_list)
else:
    print("try again")