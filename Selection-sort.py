a = [5, 1, 6, 2, 4, 3]
for x in range(len(a)):
    print("value of x :",a[x],x)
    for y in range(x+1,len(a)):
        print("value of y:",a[y], y)
        print("x iteration value of x :", a[x], x)
        if a[x]<a[y]:
            print("no swap :",a[x], a[y])
            continue
        elif a[x]>a[y]:
            a[x], a[y] = a[y], a[x]
            print("After swap: ",a[x], a[y])
            print("New array: ", a)
