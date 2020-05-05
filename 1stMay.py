
"""

#print a table

def table_new(k):
    count = 1
    prod = 1
    while count < 11:
        prod = k * count
        count = count +1
        print(prod)

table_new(8)


"""

count = 1
new = []
temp = 1
while count < 4:
    number = int(input("Enter the number: "))
    count = count + 1
    if number <= 5:
        temp = number
        new.append(temp)
    else:
        continue


print("Output less than 5: ", new)