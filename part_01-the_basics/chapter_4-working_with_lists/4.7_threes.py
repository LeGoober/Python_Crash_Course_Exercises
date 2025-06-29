"""
    This Python program requires us to create a list of multiples of 3
    from 3 to thirty and we should use a for loop to print the numbers
    in the list
"""
print("Welcome to the Print 30's Project, where we are going to print out "
      + "a list of elements that are in three's until the number 30 using the"
      + "range function,so let's go!")
range_thirty = list(range(3, 31, 3))
print("----------------------------------------------------")
print("The easy way to do this is by actually calling the range function "
      + "and just changing the parameters of the function to have the 'base "
      +"value of three and we can just increment by setting the third "
      +"parameter in order to be able to increment it to its value(i.e 1, 3, 5)")
print(range_thirty)
print("----------------------------------------------------")
print("Although this simplifies the process of actually just adding a value "
      + "to the range of values that sets the increment value as the third "
      +"parameter, we can also directly append the values to the list "
      +"through iteratng through the range and adding the values to the list")
range_thirty_2 = []
for numbers in range(3, 31):
    numbers_threes = numbers if numbers % 3 != 0 else numbers + 1
    if numbers_threes not in range_thirty_2:
        range_thirty_2.append(numbers_threes)
print("Here are the values that we stored in the numbers list: ")
print(range_thirty_2)
print("--------------------------------------------------------")