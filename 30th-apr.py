#print number of characters ina string considering space is not a character
"""
string = input("Enter string: ")
count = 0
temp = 0
for element in string:
    count = count + 1
    if element == " ":
        temp = temp + 1
count = count - temp
print(count)

"""

"""
string = input("Enter string: ")
count = 0
for element in string:
    if element != " ":
        count= count+1
print(count)


"""
"""
#Reverse the string

string = str(input("Enter the string: "))
string_new = ""
# print("value", string)
n = 0
value = len(string)
print("length of string: ", value)
value1 = string[len(string)-1]
print("value of range value: ", value1)
for element in range(len(string)):
    string_new = string_new + string[len(string) - 1 - n]
    n = n + 1
print(string_new)

"""


# find the string is palindrome or not

string = input("Enter the string :")
n = 0
for x in range(len(string)):
    print("x: ", x)
    if string[x] != string[len(string)-1 - x]:
        n = 1
if n == 1:
    print("not palindrome")
else:
    print("palindrome")

