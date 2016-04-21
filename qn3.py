import random

# initialise and define constants
NUM = 5

# initialise and define variables
array = []
integer_exists = False

# initialise array
for x in range(10):
    array.append(random.randint(0,10))

# traverse the array to search for the integer
for element in array:
    if element == NUM:
        integer_exists = True
        break

# output
print(array)
print(integer_exists)
