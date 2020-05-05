#swap the array
a = [4, 6]
prev = a[0]
next = a[1]
print(prev,next)
for x in a:
        prev = a[1]
        next = a[0]
print(prev, next)