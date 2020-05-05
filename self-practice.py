""" sum of first 1000 natural number """
"""

num = 1
sum = 0
while (num < 1001):
 sum = sum + num
 num = num + 1
print(sum)
"""

""" add the numbers in array """
"""
sum = 0
firstQuestion = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for x in firstQuestion:
     sum = sum + x
print(sum)
"""

""" print natural number till 500 """
"""
a = 1
while (a < 501):
 print(a)
 a = a + 1

"""
"""
a = 500
while (a > 0):
    print(a)
    a = a - 1
"""

"""print a. even & b. odd number till 500 starting from lowest"""
"""
a = 2
while(a < 501):
    print(a)
    a = a + 2

"""

"""
a = 1
while (a < 501):
 print (a)
 a = a + 2
"""
"""
# print multiplication of 14 from a list in which multiplication of 12 is stored
#b = {14, 28, 42, 56, 70}

"""

"""
a = (12, 24, 36, 48, 60)
b = 1
c = []
for x in a:
 d = b * 2
 c.append(x + d)
 b = b + 1
print(c)
"""

"""
a = [12, 24, 36, 48, 60]
b = 1
for x in a:
 d = b * 2
 a[b-1] = x + d
 b = b + 1
print(a)

"""

"""
Requirements:
birthday = 28/04/1992
current date = 29/03/2020
leap year in btw = {1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020} 
extra feb 29 = 8
days in a leap-year = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
days in a standard-year = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
2020-1992 = 27 years 11 months 
1 year = 365 days
27 years = 365 * 27 = 9885 days 
8 leaps years in between = 8 days
11 months days = 335 days
total days till date = 9893 days + 335 days = 10228 days

"""
#
"""
# We take user input his/her birthDate in format dd/mm/yyyy input1 =  28-04-1992 (1992)yr
# Date should be in the format dd/mm/yyyy
# System will calculate the current date and will compare it with the birthDate
# show the error message to user if the future date is entered
# show the error message to user if current date is entered
# birth date should be less than current date
# subtract the year of current from date of birth year
# Convert year into day
# calculate the number of leap year days from birth date to current date
# 



"""
"""
a = input("Enter birthYear: ")
b = input("Enter currentYear: ")
print(int(b) - int(a))

"""

"""

b = 1
while(b < 11):
    print(b*5)
    b = b+1


"""

"""
a = input()
b = 1
while(b < 11):
    c = int(a) * int(b)
    print(a,b,c)
    b = b + 1



"""

"""
a = input("Enter first number: ")
b = input("Enter second number: ")
print(int(a) * int(b))
print(int(a) / int(b))
print(int(a) + int(b))
print(int(a) -int(b))
"""
"""
c = 1
a = input("Enter first number: ")
b = input("Enter second number: ")
while (int(b) > 0):
    c = c * int(a)
    b = int(b) - 1
print (c)
"""
"""
a = [1, 2, 3, 4, 5]
b = []

for i in a:
    b.append(int(i) * int(i))
print(b)

"""
"""
a = input("Enter first number: ")
b = input("Enter second number: ")
if b > a:
    print(b)
else:
    print(a)

"""

"""
a = input("Enter the first age: ")
b = input("Enter the second age: ")
c = input("Enter the third age: ")
if a > b:
    if b > c:
        print(a,c)
    else:
        print(a,b)
elif b > c:
    if a > c:
        print(b,c)
    else:
        print(b,a)
elif a > c:
    if b > c:
        print(a,c)
    else:
        print(a,b)
"""

"""
sum = 0
year = [2019]
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
dict = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30,'May':31, 'Jun':30,'Jul':31, 'Aug':31,'Sept':30, 'Oct':31,'Nov':30, 'Dec':31}
for x in year:
    for y in month:
       sum = sum + dict[y]
print(sum)

"""

"""
a = input("Enter year: ")
if int(a)%4 > 1:
    print('Its a leap year')
else:
    print('Its not a leap year')
"""
"""



DoB = "1992-04-28"
TodayDate = "2020-04-05"
birthYear = 1992
birthMonth = 4
birthDay = 28
currentYear = 2020
currentMonth = 4
currentDay = 5
totalDays = 0
Years = [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
Months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
daysInMonths = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for year in range(1992, 2021):
    print(year)
    for month in Months:
        #Check When year is same as DOB year
        if year == birthYear:
            if month == birthMonth:
                totalDays = daysInMonths.get(birthMonth) - birthDay
                print(month)
                print(totalDays)
            elif month > birthMonth:
                totalDays = totalDays + daysInMonths.get(month)
                print(totalDays)
            else:
                print(month)
                continue
        elif year > birthYear and year < currentYear: #Check When year is greater than DOB year
            if year % 4 == 0:
                if month == 2:
                    totalDays = totalDays + daysInMonths.get(month) + 1
                else:
                    totalDays = totalDays + daysInMonths.get(month)
                print(totalDays)
            else:
                totalDays = totalDays + daysInMonths.get(month)
        else: #check when year is equal to current year
            if month < birthMonth:
                if month == 2:
                    totalDays = totalDays + daysInMonths.get(month) + 1
                else:
                    totalDays = totalDays + daysInMonths.get(month)
            elif month == birthMonth:
                totalDays = totalDays + currentDay
print(totalDays)

"""

# input - daily, weekly, monthly
# Date - 2020-04-05T00:00:00.000Z to 2020-04-06T23:59:59.999Z
# Reset period function - you have to write a function that takes input as ‘Daily’, ‘Weekly’ or
# ‘Monthly’, and based on current date returns output based on below example -
# Daily - Today’s start date time to tomorrow’s end date time
# Ex. startDateTime 2019-01-07T00:00:00.000Z
# endDateTime - 2019-01-08T23:59:59.999Z
# Weekly - This week’s start day i.e. Monday to Sunday end date time
# Ex. startDateTime 2019-01-07T00:00:00.000Z
# endDateTime - 2019-01-13T23:59:59.999Z
# Monthly - This month’s start day i.e. 01st to last day end date time i.e. month end date (30 or 31
# or 28 in case of Feburary)
# Ex. startDateTime 2019-01-01T00:00:00.000Z
# endDateTime - 2019-01-31T23:59:59.999Z
"""


starthour = 00
startmin = 00
startsec = 00
endhour = 23
endmin = 59
endsec = 59

from _datetime import datetime

todaysdate = datetime.now()
print(todaysdate)

currentyear = todaysdate.year
currentmonth = todaysdate.month
currentdate = todaysdate.day
currenthour = todaysdate.hour
currentmin = todaysdate.minute
currentsec = todaysdate.second
print(currentyear,currentmonth,currentdate,currenthour,currentmin,currentsec)

print(currentyear,currentmonth,currentdate,starthour,startmin,startsec)
print(currentyear, currentmonth, currentdate+1, endhour, endmin, endsec)

print(currentyear, currentmonth, currentdate + 7, endhour, endmin, endsec)

#monthly -
#startdate = 01, end-date = 30
startdate = currentdate - (currentdate - 1)
enddate = currentdate + (30 - currentdate)
print(currentyear, currentmonth, startdate , starthour, startmin, startsec)
print(currentyear, currentmonth, enddate , endhour, endmin, endsec)


#startday = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
#startdate = [1, 2, 3, 4, 5, 6, 7]
#daysanddate = {"Mon": 1, "Tue": 2, "Wed": 3, "Thur": 4, "Fri": 5, "Sat": 6, "Sun": 7}
#for date in startdate:
#startdate1 = int(UsersDay) - (int(UsersDay) -1)
"""

Days=0
starthour=00
startminute=00
startsecond=00
endhour=23
endminute=59
endsecond=59
UsersYear=input("Please enter any Year: ")
UsersMonth=input("Please enter any Month: ")
UsersDay=input("Please enter any Day: ")
from _datetime import datetime
todaysdate=datetime.now()
print(todaysdate)
if UsersMonth == "01" == "03" == "05" == "07" == "08" == "10" == "12":
    Days=Days + 31
    print(Days)
elif UsersMonth == "02":
    if UsersYear % 4 == 0:
        Days=Days + 29
        print(Days)
    else:
        Days=Days + 28
        print(Days)
else:
    Days=Days + 30
    print(Days)

print("Daily mission startdate: ", UsersYear, UsersMonth, UsersDay, starthour, startminute, startsecond)
print("Daily mission enddate: ", UsersYear, UsersMonth, int(UsersDay) + 1, endhour, endminute, endminute)
#print("Weekly mission startdate: ", UsersYear, UsersMonth, weeklystartdays, starthour, startminute, startsecond)
#print("Weekly mission enddate: ", UsersYear, UsersMonth, weeklyenddays, endhour, endminute, endminute)
print("Monthly mission startdate: ", UsersYear, UsersMonth, UsersDay, starthour, startminute, startsecond)
print("Monthly mission enddate: ", UsersYear, UsersMonth, Days, endhour, endminute, endminute)

"""
Number = ("Enter any number: ")
while (Number % )
"""
