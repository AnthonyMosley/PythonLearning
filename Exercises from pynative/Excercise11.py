# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
def extract_digits(num):
    return ' '.join(str(digit) for digit in reversed(str(num)))

print(extract_digits(7536))
