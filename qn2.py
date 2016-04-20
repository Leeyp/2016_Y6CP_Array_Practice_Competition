import random

# declare and initialise constant
N = 10

# declare and initialise variables and data structures
A = [6, 2, 3, 5, 5, 9, 5, 5, 5, 9]
highest = 0

# initialise array A
for x in range(N):
    A.append(random.randint(0,N-1))

# output before
print(A)

# determine the greatest number in array A
for x in A:
    if x > highest:
        highest = x

# traverse A, finding and deleting any duplicates
for x in range(highest+1):
    counter = 0
    for y in A:
        if y == x:
                counter += 1
    if counter > 1:
        for z in range(counter - 1):
            A.remove(x)

# output after
print(A)
