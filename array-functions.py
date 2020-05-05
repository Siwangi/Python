array = [9, 6, 4]
# find lowest number in the array = 4
lowestNumber = 0
count = 0
for number in array:
    if count > 0:
        if number < lowestNumber:
            lowestNumber = number
        elif number > lowestNumber:
            continue
    else:
        count = count + 1
        lowestNumber = number


print("Lowest number found", lowestNumber)





