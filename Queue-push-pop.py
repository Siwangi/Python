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
    print("Enter number to push")
    userinput = int(input("number: "))
    array.append(userinput)
    print("New array: ", array)
def Pop():
    print("Enter number to push")
    userinput = int(input("number: "))
    array.remove(userinput)
    print("New array: ", array)



def main():
    while True:
        Choice=GetChoice()
        if Choice == 'P':
            Print()
        if Choice == 'PU':
            Push()
        elif Choice == 'PO':
            Pop()
        elif Choice == "Q":
            exit()
main()





