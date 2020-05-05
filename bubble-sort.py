a = [5, 1, 6, 2, 4, 3]
count = -1
for x in range(len(a)):
    count = count + 1
    print("value of x :",a[x],x)
    for y in range(len(a)-1-count):
        print("value of y:",a[y], y)
        if a[y]<a[y+1]:
            print("no swap :",a[y], a[y+1])
            continue
        elif a[y]>a[y+1]:
            a[y], a[y+1] = a[y+1], a[y]
            print("After swap: ",a[y], a[y+1])
            print(a)