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

name = input("What's your name? ")
month = input("What month were you born in? ").lower()
year = input("What year were you born in? ")
day = input("What day were you born on? ")

todaymonth = datetime.today().month
todaymonth = month_name[todaymonth]
todaydate = datetime.today().day

if day == 31 and month == 10:
    print ("You were born on Halloween!")
elif day == todaydate and month == todaymonth:
    print ("Happy birthday!")
else:
    if month == "september" or "october" or "november":
        season = "fall"
    elif month == "december" or "january" or "february":
        season = "winter"
    elif month == "march" or "april" or "may":
        season = "spring"
    else
        season = "summer"
    if year >= 2000:
        age = "two thousands"
    if year >= 1990 and < 2000:
        age = "nineties"
    if year >= 1980 and < 1990:
        age = "eighties"
    else:
        age = "Stone Age"
    print (name + ", you are a " + season + " baby of the " + age + ".")