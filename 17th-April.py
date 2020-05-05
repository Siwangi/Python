User = int(input("Enter number:"))
a = 0
b = 1
sum = 0
while sum < User:
    number = a + b
    a = b
    b = number
    print(number)
    sum = sum + 1