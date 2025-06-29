"""
This program requires me to use a for loop in order to print out
a list of numbers ranging from 1- 20
"""
print("Learning how to count to 20 in Python is interesting because we "
      +"have many ways of doing so and I'll start with the basics"
      + "\n------------------------------------------------------")
print("So I just have to use the `range()` method in order to place the "
      + "ranges we've specified and pack them into a list using a for() loop:")
int_list = []
for int_val in range(1, 21):
    int_list.append(int_val)
print(int_list)