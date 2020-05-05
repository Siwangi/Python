"""
#print fibonacci number

number = int(input("Enter the number: "))
a = 0
b = 1
sum = 0
count = 0
while count < number:
    print(a)
    sum = a + b
    a = b
    b = sum
    count = count+1
"""
"""
# print number from 500 to 1

a = 500
num = 0
while num < 500:
    sum = a - num
    print(sum)
    num = num + 1

"""
"""
# print number from 500 to 1

a = 1
num = 0
while num < 500:
    sum = a + num
    print(sum)
    num = num +1

"""
"""
# print prime number
"""
a = int(input("Enter any number: "))
count = 1
num = 0
while count < a+1:
    if a % count == 0:
        num = num + 1
    count=count + 1
if num == 2:
    print("number is prime")
else:
    print("Number is not prime")
