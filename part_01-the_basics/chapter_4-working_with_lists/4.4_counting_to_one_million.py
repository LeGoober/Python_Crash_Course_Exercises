"""
    This program requires us to then continue on with the creation
    and manipulation of a list, and we have to make a list of numbers 
    that will store values ranging from one to one-million and we need 
    to iterate through the range and print its contents 
"""
print("Welcome to yet another program where we are going to be creating"
      + " a list of values that will store integer values ranging from"
      +" one to one-million, so here we go"
      +"\n -----------------------------------------------------------")
one_million_list = []
for int_values in range(1, 1000000):
    one_million_list.append(int_values)
print(one_million_list)