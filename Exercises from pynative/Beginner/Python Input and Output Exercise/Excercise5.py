# Initialize an empty list to store user input numbers
numbers_list = []

# Loop through a range of 5 iterations
for i in range(0, 5):
    # Print a message asking the user to enter a number at location 'i'
    print("Enter number at location", i, ":")
    
    # Store the user's input as a floating-point number and assign it to the variable 'item'
    item = float(input())
    
    # Add the 'item' (user-input number) to the end of the 'numbers_list'
    numbers_list.append(item)

# Print the complete list of user-entered numbers
print("User List:", numbers_list)
