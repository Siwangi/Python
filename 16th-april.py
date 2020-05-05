"""
name = "shivangi"
school = "Oxford"
print(" {} works at {} " .format(name,school))
"""
"""

a = [5, 0, 6, 9, 4, 12, 10, 6]


for y in range(len(a) - 1):
    if a[y] < a[y+1]:
        continue
    elif a[y] > a[y+1]:
        a[y], a[y+1] = a[y+1], a[y]
print(a)
"""

a = input("Enter any number: ")

for x in range(len(a)):
    print(x)
    if a[x] == a[len(a) - 1]:
        continue
    elif a[x] == a[len(a) - x - 1]:
        print("Its a palindrome")
    else:
        print("its not a palindrome")
