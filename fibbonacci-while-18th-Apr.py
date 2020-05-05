#print fibbonaci series

userInput = int(input("Enter number:"))
a = 0
b = 1
sum = 0
if userInput <= 0:
    print("please enter postive number")
elif userInput== 1:
    print("Number is valid")
    print(a)
else:
    print("Fibbonaci sequence:")
    while sum < userInput:
        print(a)
        term = a + b
        a = b
        b = term
        sum = sum + 1