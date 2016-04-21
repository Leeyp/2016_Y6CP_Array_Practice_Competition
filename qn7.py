import random

# declare and initialise constant
N = 10

# declare and initialise variables and data structures
A = [21, 34, 41, 22, 35]
B = [61, 34, 45, 21, 11]
duplicates = []

# initialise array A
#for x in range(N):
#   A.append(random.randint(0,N-1))

# initialise array B
#for x in range(N):
#   B.append(random.randint(0,N-1))

# traverse array A to search for any duplicates found in B
for x in A:
    if x in B:
        duplicates.append(x)

# output
print(A)
print(B)
print(duplicates)
