from datetime import datetime
from datetime import date
import time

today = date.today()


def user_birthday():
    year = int(input('what is your year of your DOB: '))
    month = int(input('what is your month of your DOB: '))
    day = int(input('what is your date of your DOB: '))

    birthday = datetime(year, month, day)
    return birthday


def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    print(today)
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday
    else:
        return birthday


bday = user_birthday()
t = calculate_dates(bday)
time_to_birthday = abs(t - today)
days = int(time_to_birthday.days)
import datetime
timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
presentyear=(datetime.datetime.now().strftime('%Y'))
presentmonth=(datetime.datetime.now().strftime('%m'))
presentdate=int(datetime.datetime.now().strftime('%d'))
deadline = f"{presentyear}-{presentmonth}-{presentdate+1} 00:00:00"
print(deadline)
start = datetime.datetime.strptime(timenow,'%Y-%m-%d %H:%M:%S')
ends = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
time=str(ends - start)
hours=datetime.datetime.strptime(time,'%H:%M:%S')
h=hours.hour
m=hours.minute
s=hours.second
print(f"Time to your Birthday is :{days} days and {h} hours {m} minutes {s} seconds")
#output
'''what is your year of your DOB: 2000
what is your month of your DOB: 03
what is your date of your DOB: 09
2022-10-20
2022-10-21 00:00:00
Time to your Birthday is :140 days and 13 hours 35 minutes 39 seconds'''

