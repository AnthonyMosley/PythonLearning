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