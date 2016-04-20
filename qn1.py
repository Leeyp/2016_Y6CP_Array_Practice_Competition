import random

# declare and initialise constant
N = 10

# declare and initialise variables and data structures
A = [] 
counting_array = []
number_of_duplicates = 0


# initialise array A
for x in range(N):
    A.append(random.randint(0,N-1))

# initialise array counting_array to record number of duplicates in A
for x in range(N):
    counting_array.append(0)

# traverse A to record frequencies of numbers in A
for x in A:
    counting_array[x] += 1

# traverse counting_array to record number of duplicates
for x in counting_array:
    if x > 1:
        number_of_duplicates += 1

# output
print(A)
print(number_of_duplicates)

             



