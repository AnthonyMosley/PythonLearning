def print_downward_half_pyramid():
    # Loop through rows from 1 to 5
    for i in range(6, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")

# Call the function to print the downward half-pyramid pattern of star (asterisk)
print_downward_half_pyramid()
