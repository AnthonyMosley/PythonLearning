def calculate_income_tax(income): # This function calculates income tax based on a given income.
    tax = 0 # Initialize the tax to zero.

    if income <= 10000: # If the income is less than or equal to $10,000, tax is $0.
        tax = 0
    elif income <= 20000: # If the income is greater than $10,000 but less than or equal to $20,000,
        tax = (income - 10000) * 0.10 # calculate the tax as 10% of the amount above $10,000.
    else: # Otherwise, if the income is greater than $20,000,
        tax = (10000 * 0) + (10000 * 0.10) + ((income - 20000) * 0.20) # calculate the tax as 10% of the first $10,000 and 20% of the amount above $20,000.

    return tax # Return the calculated income tax.

# Example usage:
income = 45000
tax_payable = calculate_income_tax(income)
print(f"The income tax payable for an income of ${income} is ${tax_payable}.")
