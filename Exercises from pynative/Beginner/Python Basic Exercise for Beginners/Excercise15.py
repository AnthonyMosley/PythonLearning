# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Expected Output
# base = 5
# exponent = 4

# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)

def exponent(base,exp):
    product = base**exp
    newString=''
    print("base = ",base)
    print("exponent = ",exp)
    print(base, " raises to the power of ",exp,"is: ",product)
    for i in range(int(exp)):
        if i == int(exp)-1:
            newString= newString + str(base)
        else:
            newString= newString + str(base)+"*"
        i+=1
    print("i.e. (",newString,"= ",product,")")
exponent(7,9)