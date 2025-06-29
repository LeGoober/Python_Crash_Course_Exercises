"""
This program requires us to store the names of at
least three kinds of Pizza we like into a list;
->We also need to use a for loop to print the Pizza
stored within the list
"""
customer_pizza_list =[]
customer_pizza = str(input("Greetings fellow Customer, I hear that you want to order some of"
+ "our famous Pizza pies;\n what are your favourite Pizzas, enter their names here or 'continue' to move on: "))

while(customer_pizza != "continue"):
    customer_pizza_list.append(customer_pizza)
    print(customer_pizza + ' is such a great choice, let\'s see what else is on your tastebuds......... ')
    customer_pizza = str(input("what are your favourite Pizzas, enter their names here or 'continue' to move on: "))

print("So now since you've been such a great customer, I will now display the list of" 
      +" all the pizzas that you've mentioned")
for pizzas in customer_pizza_list:
    print("You've selected the " + pizzas + " pizza, nice.")

print("Well that's it from our pizzeria, thanks you for your great options and we'll see you next time")