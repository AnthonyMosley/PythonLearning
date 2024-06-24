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
create_pattern(6)