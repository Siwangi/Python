"""


a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[0] = 1
a[9] = 10
length = len(a)
print(length)
mid = int(length / 2)
print(mid)
b = input("Enter any number to search: ")
if a[mid] == int(b):
    print("Search value found if input is equal than midlength value: ", int(a[mid]))
if int(b) < a[mid]:
    for search in a:
        if search == int(b):
            print("Search value found if input is less than midlength value: ", search)
if int(b) > a[mid]:
    for search in a:
        if search == int(b):
            print("Search value found if input is greater than midlength value:  ", search)


#midLength = int(length) / 2
#print(midLength)
#for search in a:
    #if midLength == b:
      #  print(midLength)
 #   if [int(midLength)] == int(b):
 #       print(a[int(midLength)])
   #     break
"""

"""

    for x in a:
        if int(b) < a[int(midLength)]:
         continue
        if int(b) > a[int(midLength)]:
         break
        if int(b) == a[int(midLength)]:
         break
if int(b) > a[int(midLength)]:

    for x in [a[5] - (length - 1)]:
        if int(b) < a[int(midLength)]:
         continue
        if int(b) > a[int(midLength)]:
         break
        if int(b) == a[int(midLength)]:
         break
if int(b) < a[int(midLength)]:
    for x in [a[0] - a[5]]:
        if int(b) < a[int(midLength)]:
         continue
        if int(b) > a[int(midLength)]:
         break
        if int(b) == a[int(midLength)]:
         break
print("User input is equal and found: ", int(b))
print("User input is greater and found: ", int(b))
print("User input is less and found: ", int(b))



#        print("Search number in less Condition: ", int(b))
"""


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Search = input("Enter any number to search: ")
arrayLength = len(a)
start = 0
end = 9
mid = int((start + end) / 2)
while start <= end:
    if int(a[mid]) > int(Search):
        end = mid - 1
        mid = int((start + end) / 2)
    elif int(a[mid]) < int(Search):
        start = mid + 1
        mid = int((start + end) / 2)
    elif int(a[mid]) == int(Search):
        print("Search Number found: ", a[mid])
        break
else:
        print("Search Number not found: ")








