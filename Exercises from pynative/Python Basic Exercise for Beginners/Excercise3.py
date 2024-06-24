#Exercise 3: Print characters from a string that are present at an even index number
#remember range(start,stop,step)
def evenIndexString():
    currentString=input("What String: ")
    print("Original String: ", currentString)
    stringLength=len(currentString)
    for i in range(0,stringLength-1,2):
        print("index[",i,"]",currentString[i])
evenIndexString()