#find the Highest number

a = [4, 9, 0, 21, 6]
num = 1
for x in range(0, len(a)-1):
    print(a[x], x)
    if a[x] < a[x+1]:
        continue
    elif a[x] > a[x+1]:
        a[x], a[x+1] = a[x+1], a[x]
print("Highest number:", a[x])