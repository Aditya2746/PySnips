import datetime
import pytz

date =  datetime.date(2020, 5, 6) # Setting Date 

# print(date)

today = datetime.date.today() # Getting Today's Date

# print(today)
# print(today.day) # getting only date
# print(today.weekday()) # getting weekday as Monday = 0
# print(today.isoweekday()) # getting weekday as Monday = 1
# print(today.month) # getting month
# print(today.year) # getting year

'''
# weekday
Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6
'''
'''

#isoweekday
Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6 
'''

tdelta = datetime.timedelta(days=7)
# parameters that can be passed to datetime.timedelta()
'''
 days=0,
 seconds=0, 
 microseconds=0, 
 milliseconds=0, 
 minutes=0, 
 hours=0, 
 weeks=0
'''
# print(today + tdelta)

bday = datetime.date(2021, 4, 27)

till_bday  = bday - today

# print(till_bday.days) # getting the number of day 
# print(till_bday.total_seconds()) # getting the number of seconds


time = datetime.time(9, 30, 45, 1000)

# print(time)
# print(time.hour)
# print(time.minute)
# print(time.second)
# print(time.microsecond)

date_and_time = datetime.datetime(2021, 1, 30, 14, 25, 40)

# print(date_and_time)
# print(date_and_time.date())
# print(date_and_time.time())
# print(date_and_time.day)
# print(date_and_time.weekday())
# print(date_and_time.isoweekday())
# print(date_and_time.year)
# print(date_and_time.month)
# print(date_and_time.hour)
# print(date_and_time.minute)
# print(date_and_time.second)
# print(date_and_time.microsecond)

# print(date_and_time + tdelta)

dt = datetime.datetime(2021, 2, 3, 14, 12, 25, tzinfo=pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_ind = dt_now.astimezone(pytz.timezone('Asia/Kolkata')) 

# print(dt)
# print(dt_now)
# print(dt_ind)   

# adding timezone to navie date
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
# and then changing its tz
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))

# print(dt_ind.isoformat())
# print(dt_ind.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt_from_str = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt_from_str)

# strftime - Datetime to String
# strptime - String to Datetime