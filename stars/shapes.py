num = int(input("Kac satırlık olsun: "))

# triangle of stars
for i in range(0, num):
    for j in range(i+1):
        print("*", end='')
    print()

# Result:
# *
# **
# ***
# ****
# *****

# -----------------------------------
# inverted triangle of stars
for i in range(num, 0, -1):
    for j in range(i):
        print("*", end='')
    print()

# Result:
# *****
# ****
# ***
# **
# *

# -----------------------------------
# a triangle of stars

for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(" ", end='')
    for j in range(1, 2*i):
        print("*", end='')
    print()

# Result:
#      *
#     ***
#    *****
#   *******
#  *********

# -----------------------------------
# a inverted triangle of stars
for i in range(num, 0, -1):
    for j in range(1, num - i + 1):
        print(" ", end='')
    for k in range(1, 2 * i):
        print("*", end='')
    print()

# Result:
# *********
#  *******
#   *****
#    ***
#     *


# -----------------------------------
# a diamond of stars

for i in range(1, num + 1):
    for j in range(1, num - i + 1):
        print(" ", end='')
    for k in range(1, 2 * i):
        print("*", end='')
    print()
for i in range(num-1, 0, -1): # en uzun satırdan bir tane olsun diye num-1 den başlandı
    for j in range(1, num - i + 1):
        print(" ", end='')
    for k in range(1, 2 * i):
        print("*", end='')
    print()

# Result:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# -----------------------------------
# a solid square of stars

for i in range(num):
    for j in range(num):
        print("*", end="")
    print()

# Result:
# *****
# *****
# *****
# *****
# *****


# -----------------------------------
# a solid square of stars

for i in range(num):
    for j in range(num):
        if i == 0 or j == 0:
            print("*", end="")
        elif i == num -1 or j == num -1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Result:
# *****
# *   *
# *   *
# *   *
# *****

for i in range(num):
    for j in range(num):
        if i == 0 or i == num - 1:
            print("-", end="")
        elif j == num - 1 or j == 0:
            print("|", end="")
        else:
            print(" ", end="")
    print()

# Result:
# -----
# |   |
# |   |
# |   |
# -----
