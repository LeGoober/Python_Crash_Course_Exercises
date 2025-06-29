"""
    In this program we are working with Lists and this time we are tasked
    with using one of the programs I'd written in this chapter and adding
    more code to the program to achieve the following functionality with
    the lists:
    ->print the message: the first three items in the list, then using a 
    slice to print those first three items,
    ->print the message: three items from the middle of the list are...
    then use a slice to pring out those middle items,
    ->print the message, the last three items are... and use a slice to 
    print out those last three items.
"""
print("Welcome to the Slices program, where we integrate the "
      + "functionalities of our Pizza Program with the ability to select "
      + "the items in the list")
print("-----------------------------------------------------------------")

customer_pizza_list =[]
customer_pizza = str(input("Greetings fellow Customer, I hear that you " 
    +"want to order some of our famous Pizza pies; "
    +"\n what are your favourite Pizzas, \nEnter their "
    +"names here or 'continue' to move on: "))

while(customer_pizza != "continue"):
    customer_pizza_list.append(customer_pizza)
    print(customer_pizza + ' is such a great choice, let\'s see what else '
    + 'is on your tastebuds......... ')
    print("-----------------------------------------------------------------")
    
    customer_pizza = str(input("What are your favourite Pizzas, enter "
    +"their names here or 'continue' to move on: "))
print("-----------------------------------------------------------------")

print("So now since you've been such a great customer, I will now display "
    +"the list of all the pizzas that you've mentioned")
for pizzas in customer_pizza_list:
    print("You've selected the: " + pizzas + " pizza, nice.")

customer_pizza_2 = str(input("Would you like to select any more pizza's or "
    +"shall we contiue on with showing you the first three pizzas, the "
    +"pizza's in the middle of the list and the last three pizzas \n"
    +"-----------------------------------------------------------------"
    +"\nEnter 'continue' here or add your final selection: "))
while customer_pizza_2 != "continue":
    customer_pizza_list.append(customer_pizza_2)
    print(customer_pizza_2 + ' is such a great choice, let\'s see what else '
    + 'is on your tastebuds......... ')
    print("-----------------------------------------------------------------")
    customer_pizza_2 = str(input("What are your favourite Pizzas, enter "
    +"their names here or 'continue' to move on: "))

print("These are a lot of Pizza's ; P\n All the pizzas in the list are:")
for pizzas in customer_pizza_list:
    print("You've selected the: " + pizzas + " pizza, nice.")

print("-----------------------------------------------------------------")
print("The First three Pizza's in your selection are:")
for pizzas in customer_pizza_list[:3]:
    print(pizzas.title())

print("-----------------------------------------------------------------")
print("The Middle three Pizza's in your selection are:")
customer_pizza_list_middle = len(customer_pizza_list) // 2
middle_three_elements = customer_pizza_list[customer_pizza_list_middle -1 : customer_pizza_list_middle + 2]
for pizzas in middle_three_elements:
    print(pizzas.title())


print("-----------------------------------------------------------------")
print("The Last three Pizza's in your selection are:")
for pizzas in customer_pizza_list[-3:]:
    print(pizzas.title())
