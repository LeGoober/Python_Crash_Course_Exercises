"""
    With the following Python program we'll be creating yet another simple
    numerical list where we are going to change the third parameter within
    the range function in order to count in odd numbers
"""
print("Welcome to my Python project where we are working with a list "
      +"will store numerical values that are odd numbers and for the "
      +"first example we will just change the parameters of the range()"
      +"function that will allow us to then ensure that we are incrementing"
      +"the value we are passing into the list(i.e. range(1, 16, 2))")
numbers_list = []
for numbers in range(1, 16, 2):
    numbers_list.append(numbers)
print("Here are the values that we stored in the numbers list: ")
print(numbers_list)

print("--------------------------------------------------------"
      +"\n There are various ways in which we can manipulate the ways "
      +"we add values into a list and now we're going to continue from "
      +"the range of numbers we had stored previously and the only major "
      +"that we can make is call a for loop and iterate through a range of "
      +"values and perform the function of transforming the values to odd\n")
print("--------------------------------------------------------")
numbers_list_1 = []
for numbers_1 in range(17, 25):
    number_odd = numbers_1 if numbers_1 % 2 != 0 else numbers_1 + 1
    if number_odd not in numbers_list_1:
        numbers_list_1.append(number_odd)
print("Here are the values that we stored in the numbers list: ")
print(numbers_list_1)
print("--------------------------------------------------------")
