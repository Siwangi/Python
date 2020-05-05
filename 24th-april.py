#print the average of the array
"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(a)
print(length)
sum = 0
for x in a:
    sum = sum + x
avg = sum / length
print(avg)
"""
"""
# print the avg of an array given by user

length = int(input("Enter the length of the array: "))
count = 0
array = []
sum = 0
avg = 0
while count<length:
    a = int(input("Enter the number: "))
    count=count + 1
    array.append(a)
print("array: ", array)
for x in array:
    sum = sum + int(x)
    avg = sum / len(array)
print("Average of the array: ", avg)

"""


#print an array given by user and find how many vowels are in it

length = int(input("Enter length of the array: "))
print(length)
count = 0
sum = 0
array = []
while count < length:
    a =input("Enter character: ")
    count = count +1
    array.append(a)
print(array)
for x in array:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        sum = sum + 1
print(sum)