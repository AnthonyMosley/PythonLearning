#Exercise 7: Return the count of a given substring from a string
def subStringCount(inputString,subString):
    return inputString.lower().count(subString)
print("Emma appeared",subStringCount("Emma is good developer. Emma is a writer", "emma"),"times")