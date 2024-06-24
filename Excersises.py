#all exercises are from https://pynative.com/python-basic-exercise-for-beginners/
def Exercise1():
    number1 = int(input("Number 1:"))
    number2 = int(input("Number 2:"))
    #Exercise 1: Calculate the multiplication and sum of two numbers
    def multiplication_or_sum(number1,number2):
        product = number1 * number2
        if product <= 1000:
            return product
        else:
            return number1+number2
    print(multiplication_or_sum(number1,number2))
def Exercise2():
    #Exercise 2: Print the sum of the current number and the previous number
    def sumofcurrentandprevious():
        i=0
        previousNumber = 0
        print("Printing current and previous number sum in a range(10)")
        for i in range(10):
            currentNumber = i
            if i ==0:
                previousNumber = 0
            else:
                previousNumber = i-1
            sum = currentNumber + previousNumber
            #print(sum)
            i+=1
            print("Current Number ",currentNumber, "Previous Number ",previousNumber, "Sum: ",sum)
    sumofcurrentandprevious()
def Exercise3():
    #Exercise 3: Print characters from a string that are present at an even index number
    #remember range(start,stop,step)
    def evenIndexString():
        currentString=input("What String: ")
        print("Original String: ", currentString)
        stringLength=len(currentString)
        for i in range(0,stringLength-1,2):
            print("index[",i,"]",currentString[i])
    evenIndexString()
def Exercise4():
#Exercise 4: Remove first n characters from a string
#remember Slice IE string[start:end:step]
    def remove_chars(string, x):
        for i in range(x): 
            string = string[1:]
        return string
    print(remove_chars(input("What String would you like: "),int(input("How much would you like to remove from the beginning: "))))
        #How to use: print(remove_chars(input('What string: '),int(input("How many Numbers: "))))
def Exercise5():
    #Exercise 5: Check if the first and last number of a list is the same
    numbersX=[10,20,30,40,10]
    numbersY=[75,65,35,75,30]
    def firstLastSame(list1):   
        if list1[0] == list1[-1]:  
            return True     
        else:                     
            return False
    print("Given List: ",numbersX)
    print("Result is",firstLastSame(numbersX))
    print("Given List: ",numbersY)
    print("Result is",firstLastSame(numbersY))
def Exercise6():
    #Exercise 6: Display numbers divisible by 5 from a list
    #Iterate the given list of numbers and print only those numbers which are divisible by 5
    givenList= [10,20,33,46,55]
    def divisibleBy5(list):
        for i in range(len(list)):
            if list[i] % 5 == 0:
                print(list[i])
    divisibleBy5(givenList)
def Exercise7():
    #Exercise 7: Return the count of a given substring from a string
    def subStringCount(inputString,subString):
        return inputString.lower().count(subString)
    print("Emma appeared",subStringCount("Emma is good developer. Emma is a writer", "emma"),"times")
def Exercise8(x):
    # Exercise 8: Print the following pattern:
    #   1
    #   2 2
    #   3 3 3
    #   4 4 4 4
    #   5 5 5 5 5
    def create_pattern(x):
        for number in range(x):
            for i in range(number):
                print(number, end='  ')
            print('\n')
    create_pattern(x)
def Exercise9():
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
def Exercise10():
    # Exercise 10: Create a new list from two list using the following condition
    # Create a new list from two list using the following condition
    # Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
    list1= [10,20,25,30,35]
    list2= [40,45,60,75,90]
    def combineList(list1,list2):
        newlist= []
        for i in range(len(list1)):
            if list1[i] % 2 != 0:
                newlist.append(list1[i])
        for i in range(len(list2)):
            if list2[i] % 2 == 0:
                newlist.append(list2[i])
        return newlist
    print(combineList(list1,list2))
def Exercise11():
    # Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
    # For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits
    