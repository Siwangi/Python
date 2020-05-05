
"""
# print a^b if user gives input of 2 number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
prod = 1
count = 0
while count < b:
    prod = prod * a
    count = count+1
print(prod)
"""
"""
# print in same array multiplication of each element by 2

a = [2, 3, 4, 5]
for x in range(len(a)):
    a[x] = a[x]*2
print(a)


"""
#reverse the array
a = [1,2,3,4,5,10,12]
n = 1
b = []
for x in range(len(a)):
    b.append(a[len(a) - n])
    n = n+1
print(b)