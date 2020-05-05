#print number is Armstrong

number = int(input("Enter number to check if its Armstrong: "))
sum = 0
temp = number

while number > 0:
    num = number % 10
    print("num:", num)
    sum = sum + num * num * num
    print("sum :", sum)
    number = int(number / 10)
    print("number: ",number)
if sum == temp:
    print("Number is an Armstrong")
else:
    print("Number is not an Armstrong")



