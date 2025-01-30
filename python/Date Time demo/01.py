import datetime

# class
# datetime.date                     #for working with dates
# datetime.time                      #for working with time
# datetime.timedelta      #represents the duration
# datetime.tzinfo         #base class for dealing with the zone.


# current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)


#get current date only
date = datetime.date.today()
print(date)

#specific date
date = datetime.date(2025,5,10)
print(date)


#specific time
date = datetime.time(14,30,25)
print(date)


#extracting data and time components
now = datetime.datetime.now()
print("Year",now.year)
print("Month",now.month)
print("Day",now.day)
print("Hour",now.hour)
print("minute",now.minute)
print("Second",now.second)


#Date arithmetic with timedelta()
#add and subtract days



today = datetime.date.today()
future_date = today+datetime.timedelta(days=10)
past_date = today-datetime.timedelta(days=10)
print("10 days after today: ",future_date)
print("10 days before today: ",past_date)

