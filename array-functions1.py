array = [1, 12, 89, 11, 89]
# find highest number in the array = 4
highestNumber = 0
count = 0
for number in array:
    if count > 0:
        if number < highestNumber:
            continue
        elif number > highestNumber:
            highestNumber = number

    else:
        count = count + 1
        highestNumber = number


print("Highest number found", highestNumber)





