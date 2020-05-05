# sort in ascending order
a=[30, 7, 3, 11, 9, 0, 6, 10]
length = len(a)
print(length)
for x in range(len(a)):
    for y in range(0, len(a) - x - 1):
            if a[y] > a[y+1]:
                continue
            elif a[y] < a[y+1]:
                a[y], a[y+1] = a[y+1], a[y]
print(a)

"""
# print using 2 loops
i =['a', 'b', 'c', 'd', 'e']
j = [1, 2, 3, 4, 5]
for x in i:
    for y in j:
        print(x,y)

"""


# print using 2 loops
# i =['a', 'b', 'c', 'd', 'e']
# j = [1, 2, 3, 4, 5]
# count = -1
# length = len(i)
# for x in i:
#     count = count + 1
#     for y in range(1, len(j) - count + 1):
#         print(x,y)
