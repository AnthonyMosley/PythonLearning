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