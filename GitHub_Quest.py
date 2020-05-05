"""

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

value = " "
count = 2000
while count < 3201:
    if count % 7 == 0 and count % 5 != 0:
        value=value + str(count) + " , "
    count = count + 1
print("Numbers: ", value)
"""

"""
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

dict = {}
for key in range(1, 8):
    dict[key] = key * key
print(dict)
"""



