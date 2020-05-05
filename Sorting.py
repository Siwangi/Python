"""
a = [3, 5, 1, 0, 7, 9]
for j in range(len(a)):
    for i in range(0, len(a)-j-1):
        if a[i] > a[i+1]:
            a[i] = a[i+1]
            a[i+1] = a[i]
print(a)
"""
"""
a = [3, 2, 6, 4, 9, 7]

for x in range(len(a)):
    print(a[x], x)
    for y in range(len(a)-x-1):
        if a[y] > a[y+1]:
            a[y], a[y+1] = a[y+1], a[y]
            print(a)

"""

# a = [5, 1, 6, 9, 4, 12]
# length = len(a)
# print(length)
# for x in range(len(a)):
#     print("value of x:", a[x], x)
#     for y in range(1, len(a)):
#             print("value of y:", a[y], y)
#             if a[x] < a[y]:
#                 print(a[x], a[y])
#                 continue
#             elif a[x] > a[y]:
#                 a[x], a[y] = a[y], a[x]
#                 print(a)


a=[7, 3, 11, 20, 2, 0, 10]
length=len(a)
for x in range(len(a)-1, 0, -1):
    for y in range(x):
        if a[y] < a[y+1]:
            continue
        elif a[y] > a[y+1]:
            temp = a[y]
            a[y] = a[y+1]
            a[y+1] = temp
            print(a)
