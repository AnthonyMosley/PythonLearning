#Exercise 6: Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5
givenList= [10,20,33,46,55]
def divisibleBy5(list):
    for i in range(len(list)):
        if list[i] % 5 == 0:
            print(list[i])
divisibleBy5(givenList)