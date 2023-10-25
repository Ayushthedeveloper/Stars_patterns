
# spuare pattern
n = 5
for j in range(n): #outer loop determine the row
    for i in range(n):#inner loop detremine column
        print("*", end="  ")
    print()
print()

#  increasing triangle pattern

n = 5
for j in range(n):
    for i in range(j+1): #range of inner loop will be (j+1)
        print("*", end="  ")
    print()
print()
# decrteasing triangle pattern

n = 5
for j in range(n):
    for i in range(j, n): # range of inner loop will be (i, n)
        print("*", end="  ")
    print()
print()
# right side increasing triangle

n = 5
for j in range(n):
    for i in  range(j,n):
        print(" ", end=" ") # decreasing triangle with space
    for i in range(j+1):
        print("*", end=" ") # increasing triangle with star
    print()
print()

# right side decreasing triangle

n = 5
for j in range(n):
    for i in range(j):
        print(" ", end=" ")
    for i in range(j, n):
        print("*", end=" ")
    print()
print()

# HILL PATTERN

n = 5
for j in range(n):
    for i in range(j, n):
        print(" ", end=" ")
    for i in range(j+1):
        print("*", end=" ")
    for i in range(j):
        print("*", end=" ")
    print()
print()

# REVERSE HILL PATTERN

n = 5
for j in range(n):
    for i in range(j+1):
        print(" ", end=" ")
    for i in range(j, n-1):
        print("*", end=" ")
    for i in range(j, n):
        print("*", end=" ")
    print()
print()

# DIAMOND PATTERN
n = 5
for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()

# BUTTTERFLY PATTERN

n = 4
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i,n-1):
        print(" ", end=" ")
    for j in range(i,n):
        print(" ", end= " ")
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    for j in range(i):
        print(" ", end=" ")
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()

