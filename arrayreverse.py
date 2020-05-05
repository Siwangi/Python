a = [1, 2, 3, 4, 5, 6, 10, 14]
#reverse the array
n = 0
b = []
length = len(a)
print(length)
for x in a:
    length1 = length - n
    b.append(a[length1-1])
    n = n + 1
print(b)

