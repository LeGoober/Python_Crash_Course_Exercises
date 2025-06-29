bicycles = ["Trek", "Cannondale", "Redline","Specialized"]
print('The List of bicycles: ', bicycles)

print("The first bicycle in the list we use the Index of (bicyclesp[0]): " + bicycles[0])
print("To access the last element within the List, I'd use '-1' as the index: " + bicycles[-1])

user_input = str(input("Enter the name of the bicycle you'd want to add to the list(or X to stop): "))
while user_input != 'x':
    bicycles.append(user_input)
    print(bicycles)
    user_input = str(input("Enter the name of the bicycle you'd want to add to the list(or X to stop): "))

user_input_2 = str(input("To continue with the program, we can delete the values stored in the List using the 'remove() method," +
      "\n Enter the name of the Bicycle you want to delete from the List(or 'x' to end this segment): "))
while user_input_2 != 'x':
    bicycles.remove(user_input_2)
    print(bicycles)
    user_input_2 = str(input("To continue with the program, we can delete the values stored in the List using the 'remove() method'," +
      "\n Enter the name of the Bicycle you want to delete from the List(or 'x' to end this segment): "))