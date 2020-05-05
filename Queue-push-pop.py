def GetChoice():
    print()
    print(" P == Print the array ")
    print(" PU == Push in the array")
    print(" PO == Pop in the array")
    print(" Q == Quit")
    print()
    UserChoice = input("Enter choice:  ")
    print()
    UserChoice = UserChoice.upper()
    return UserChoice
array = [1, 2, 3, 4, 5]

def Print():
    print("array: ", array)

def Push():
    count = 0
    print("Enter number to push")
    try:
        userinput = int(input("number: "))
        array.append(userinput)
        print("New array: ", array)
    except ValueError:
        print("You can only push number in this array")
def Pop():
    count = 0
    print("Enter number to pop")
    try:
        userinput = int(input("number: "))
        for i in array:
            if userinput == i:
                count = 1
        if count == 1:
            array.remove(userinput)
            print("New array: ", array)
        elif len(array) == 0:
            print("Array is empty")

        else:
            print("Number is not in array")
    except ValueError:
        print("You can only pop number in this array")



def main():
    while True:
        Choice=GetChoice()
        if Choice == 'P':
            Print()
        if Choice == 'PU':
            Push()
        elif Choice == 'PO':
            Pop()
        # elif Choice == " ":

        elif Choice == "Q":
            exit()
main()





