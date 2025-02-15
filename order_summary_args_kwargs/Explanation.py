# Question:

# Write a function named order_summary that receives the following parameters:
# Write a function named order_summary that receives the following parameters:
# def order_summary(*args, **kwargs):
# A list of ordered dishes (using *args) and customer requirements
# (such as name, table number, and special notes) (using **kwargs).
# The function should print the list of dishes separately and the customer requirements separately.
# Add a check: if no dishes are ordered, print an error message.
# If the customer does not specify the table number in **kwargs,
# print a random table number between 1 and 20.
#------------------------------------------------------------------------------------------------

### Explanation
# - The function checks if any dishes were passed; if not, it prints an error message.
# - It prints the ordered dishes line by line.
# - For customer requirements, it retrieves the table number, name, and special notes from `**kwargs`,
# providing defaults where necessary (a random table number between 1-20 if not specified,
# and default values for name and notes).
# - The example usage demonstrates how to call the function with various parameters.**



