import random

# declare and initialise constant
N = 10

# declare and initialise variables and data structures
A = [1, 1, 2, 2, 3, 4, 4, 5, 5] 
counting_array = []
not_duplicated = None


# initialise array A
#for x in range(N):
#   A.append(random.randint(0,N-1))

# initialise array counting_array to record number of duplicates in A
for x in range(N):
    counting_array.append(0)

# traverse A to record frequencies of numbers in A
for x in A:
    counting_array[x] += 1

print(counting_array)
# traverse counting_array to record number that is not duplicated
for x in counting_array:
    if x >= 1 and x != 2:
        not_duplicated = counting_array.index(x)

# output
print(A)
print(not_duplicated)
