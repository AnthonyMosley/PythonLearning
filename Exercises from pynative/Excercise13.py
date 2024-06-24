def print_multiplication_table():
    # Loop through numbers 1 to 10
    for i in range(1, 11):
        # Loop through numbers 1 to 10 for each row
        for j in range(1, 11):
            # Print the product and use end=' ' to keep it on the same line
            print(f"{i * j:4}", end=' ')
        # Print a newline character after each row
        print()

# Call the function to print the multiplication table
print_multiplication_table()
