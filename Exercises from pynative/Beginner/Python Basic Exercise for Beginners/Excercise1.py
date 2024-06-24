# Take two numbers as input from user
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

# Function to calculate either multiplication or sum of two numbers based on the result being <= 1000
def multiplication_or_sum(number1, number2):
    # Calculate product
    product = number1 * number2
    
    if product <= 1000:
        return product
    else:
        return number1 + number2

# Call function and print the result
print(multiplication_or_sum(number1, number2))
