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
from typing import List
"""
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


dateOfbirth = input("Enter your Date of birth: ")
print('date of birth entered: ', dateOfbirth)
from datetime import date
today = date.today()
print("Today's date:", today)
if dateOfbirth > today:
    print("birth date should be less than today's date")

"""


"""
 days=0
years=["2019"]
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
MonthAndDays={'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30,
              'Oct': 31, 'Nov': 30, 'Dec': 31}
for year in years:
    for month in months:
        days=days + MonthAndDays.get(month)
        print(days)

 
 """

"""
import datetime
currentdate = datetime.datetime.now()
print(currentdate)
dob = datetime.datetime(1980, 5, 16)
print(dob)

year = currentdate.year - dob.year
month = currentdate.month - dob.month
days = currentdate.day - dob.day

if month < 0:
   year = year - 1
   month = month + 12

if days < 0:
    month = month - 1
    days = days + 31

print(year, month, days)
"""
"""
dateOfbirth = input("Enter your Date of birth: ")
print('Date of birth entered: ', dateOfbirth)
from datetime import date
today = date.today()
print("Today's date:", today)
for year in
birthYear = 1992
todayYear = 2020
if birthYear > todayYear:
    print("Error Message: Birth date should be less than today's date")

"""

totalDays = 0
Years = [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
Year = - 1
Month = 0
for x in Years:
    Year = Year + 1
    if x % 4 == 0:
      totalDays = totalDays + 366
    if x == 1992:
       if Month == 'Jan':
           totalDays = totalDays + 0
if Month == 'Feb':
       totalDays = totalDays + 0
if Month == 'Mar':
       totalDays = totalDays + 0
if Month == 'Apr':
       totalDays = totalDays + 30 - 2
if Month == 'May':
       totalDays = totalDays + 31
if Month == 'Jun':
       totalDays=totalDays + 30
if Month == 'Jul':
       totalDays=totalDays + 31
if Month == 'Aug':
       totalDays=totalDays + 31
if Month == 'Sept':
       totalDays=totalDays + 30
if Month == 'Oct':
       totalDays=totalDays + 31
if Month == 'Nov':
       totalDays=totalDays + 30
if Month == 'Dec':
       totalDays=totalDays + 31
elif x % 4 != 0:
        totalDays = totalDays + 365
        Year = Year - 1
if x == 2020:
 if Month == 'Jan':
    totalDays=totalDays + 31
if Month == 'Feb':
    totalDays=totalDays + 29
if Month == 'Mar':
    totalDays=totalDays + 31
if Month == 'Apr':
    totalDays=totalDays + 5


print(totalDays)


