# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
# Expected Output:
# original number 121
# Yes. given number is palindrome number
# original number 125
# No. given number is not palindrome number
def palindromeChecker():
    number = input("What Number are we checking?")
    reversed_number = str(number)[::-1]
    if reversed_number == str(number):
        print("original number", number,'\n',"Yes. given number is palindrome number")
        return True
    else:
        print("original number", number,'\n',"No. given number is not palindrome number")
        return False
palindromeChecker()