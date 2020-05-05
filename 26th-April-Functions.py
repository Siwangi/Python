
"""
def siwangi(fname , lname):
    print(fname + " " + lname)

siwangi("Nikhil","Saha")


def sum(a , b):
    return (a+b)


x = sum(5,8)
y = x * 10
print(y)

"""
# find factorial of a number using recursive function
"""
def tri_recursion(k):
  if(k > 1):
    result = k * tri_recursion(k - 1)
    print(result)
  else:
    result = 1
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""
"""
def cal_number(k):
    if(k > 0):
        print(k)
        result = cal_number(k-1)
    else:
        result = 1
    return result
print("Number from 0 to 100")
cal_number(100)
"""

def fibonacci_series(i, j):
    if (j < 100):
        print(i+j)
        fibonacci_series(j,i + j)
print("fibonacci series: ")
fibonacci_series(1, 1)