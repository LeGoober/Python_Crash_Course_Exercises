"""
    This is the fourth program that we are tasked  to try and this 
    program requires me to make a listof numbers from 1 to 1000000
    and with that we need to use the min() and max()  to make sure 
    that our list starts from one and ends at one million.
    ->and we then also use the sum() in order to see how quick the 
    interpreter will total the values
"""
print("We are here with another program where we have to use the "
      +"that we're specifically designed to process numerical data "
      + "and they're the following:"
      +"\n1. the min() function, \n2. the max() function, \n3. the sum()"
      +"\nSo let's see how the Python intepreter will deal with a list of "
      +"a million items")
print("--------------------------------------------------------------")
one_milli_items = []
for int_values in range(1, 1000001):
    one_milli_items.append(int_values)

print("The Minimum value of our list is: "
    + str(min(one_milli_items))
    +"\n------------------------------")
print("The Maximum value of our list is: "
    + str(max(one_milli_items))
    + "\n-----------------------------")
print("The sum of all the values that are stored within the range is:"
    + str(sum(one_milli_items))
    + "\n------------------------------")

print("And if you want to see the rest of the list here it is: ")