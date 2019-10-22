# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date one week from the date entered
from datetime import datetime, timedelta
today = datetime.now()
print(today)
one_day= timedelta(days=1)
yesterday= today - one_day
print(yesterday)
raindomdate = input("can u give a date(dd/mm/yyyy)")
date = datetime.strptime(raindomdate, '%d/%m/%Y')
week = timedelta(weeks=1)
week_later = date + week
print('One week later it will be: ' + str(week_later))
