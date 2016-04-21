import random

# initialise and define variables
array = []
highest = 0
lowest = 99

# initialise array
for x in range(10):
    array.append(random.randint(0,10))

# traverse the array to search for the highest and lowest
for element in array:
    if element > highest:
        highest = element
    if element < lowest:
        lowest = element

# output
print(array)
print(highest)
print(lowest)
