a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=input("Enter any number to search: ")
for searchNumber in a:
    if searchNumber == int(b):
        print("Search number found:", searchNumber)
        break
