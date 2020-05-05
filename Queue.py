

def GetChoice():
    #Function to present the user menu and get their choice

    #local variables

    UserChoice = str()

    #Display menu and get choice

    print()
    print("Select one of the options listed below:  ")
    print("\tP\t==\tPrint Data")
    print("\tA\t==\tGet Averages")
    print("\tAZ\t==\tAverage Per Zone")
    print("\tAL\t==\tAbove Levels by Zone")
    print("\tBL\t==\tBelow Levels")
    print("\tQ\t==\tQuit")
    print()
    UserChoice = input("Enter choice:  ")
    print()
    UserChoice = UserChoice.upper()

    return UserChoice

def PrintData():
    print("test, test, test")

def AverageLevels():
    print("test, test, test")

def AveragePerZone():
    print("test, test, test")

def AboveLevels():
    print("test, test, test")

def BelowLevels():
    print("test, test, test")

def main():
    Choice = str()

    #call GetChoice function


    #Loop until user quits
while True:
    Choice=GetChoice()

    if Choice == 'P':
        PrintData()
    elif Choice == 'A':
        AverageLevels()
    elif Choice == 'AZ':
        AveragePerZone()
    elif Choice == 'AL':
        AboveLevels()
    elif Choice == 'BL':
        BelowLevels()
    elif Choice == "Q":
        exit()

main()
