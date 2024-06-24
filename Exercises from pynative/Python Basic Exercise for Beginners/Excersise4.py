#Exercise 4: Remove first n characters from a string
#remember Slice IE string[start:end:step]
def remove_chars(string, x):
    for i in range(x): 
        string = string[1:]
    return string
print(remove_chars(input("What String would you like: "),int(input("How much would you like to remove from the beginning: "))))
    #How to use: print(remove_chars(input('What string: '),int(input("How many Numbers: "))))
