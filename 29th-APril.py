"""

#take two inputs and swap using variablr
a = input("Enter first number: ")
b = input("Enter second number: ")
temp = a
a = b
b = temp
print(a, b)
"""
"""

"""
"""
#swap keys values

dict = {"key1": 3, "key2": 4, "key3": 5, "key4": 6}
dict_1 = {}
temp = 0
for key in dict:
    temp = key
    key = dict[key]
    dict[key] = temp
    dict.update(dict)
    print(dict)

# for key in dict:
#     print(key, dict[key])
#     temp = key
#     key = dict[key]
#     dict[key] = temp
#     print(key, dict[key])

# for (key, value) in dict.items():
#     print(key, value)
#     temp = dict[key]
#     dict[key] = key
#     key = temp
#     print(key, dict[key])
"""
"""
# print prime number

User = int(input("Enter any number: "))
count = 1
sum = 0
while count <= User:
    print("count",count)
    if User % count == 0:
        sum = sum + 1
        print("Sum added: ",sum)
    count = count + 1
    print("Count increase: ", count)
if sum == 2:
        print("Number is prime")
else:
    print("Number is not prime")

"""
"""
# print number of character in a word

word = str(input("Enter the word: "))
count = 0
# print(word)
# length = len(word)
# print("Number of characters in word: ", length)
# Not using function - len
for element in word:
    count = count+1
print("Number of characters in word: ", count)
"""


"""
# print number of words in a sentence
# length = len(sentence)
# print("Number of characters in the sentence: ", length)

sentence = str(input("Write a Sentence: "))
count = 0
for word in sentence:
    if word == " ":
        count = count + 1
print(count+1)

"""


