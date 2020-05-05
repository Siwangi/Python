#print prime number
i = int(input("enter any number: "))
n = 1
value = 0
while n < i+1:
    if i % n == 0:
        value = value + 1
        n = n + 1
    else:
        n = n + 1
if value > 2:
    print("number is composite")
else:
    print("number is not")
