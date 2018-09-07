"""
birthday.py
Author: Andrew Chen
Credit: none
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name

name = input("Hello, what is your name? ")
month = input("Hi " + name + ", what was the name of the month you were born in? ").lower()
year = int(input("And what year were you born in, " + name + "? "))
day = int(input("And the day? "))

todaymonth = datetime.today().month
todaymonth = month_name[todaymonth].lower()
todaydate = datetime.today().day

if day == 31 and month == "october":
    print ("You were born on Halloween!")
elif day == todaydate and month == todaymonth:
    print ("Happy birthday!")
else:
    if month in ["september", "october", "november"]:
        season = "fall"
    elif month in ["december", "january", "february"]:
        season = "winter"
    elif month in ["march", "april", "may"]:
        season = "spring"
    else:
        season = "summer"
    if year >= 2000:
        age = "two thousands"
    elif year >= 1990 and year < 2000:
        age = "nineties"
    elif year >= 1980 and year < 1990:
        age = "eighties"
    else:
        age = "Stone Age"
    print (name + ", you are a " + season + " baby of the " + age + ".")