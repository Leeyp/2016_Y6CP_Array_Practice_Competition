import random

# declare and initialise constant
N = 10
K = 3

# declare and initialise variables and data structures
A = []
small_numbers = []

# initialise array A
for x in range(N):
   A.append(random.randint(0,N-1))

# initialise array small_numbers to record the small numbers in A
for x in range(K):
   small_numbers.append(99)

# traverse array A to search for smallest numbrs
for x in A:
    for y in range(K):
        if x < small_numbers[y]:
            small_numbers[y] = x
            break
# output
print(A)
print(small_numbers[K-1])
