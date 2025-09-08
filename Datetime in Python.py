import datetime
'''today = datetime.datetime.today()
christmas = datetime.datetime(2025, 12, 25)
number_of_days = christmas - today
print(f"Number of Days till Christmas {number_of_days.days}")'''
year_of_next_birthday = int(input("Enter the Year of your Next Birthday: "))
month_of_next_birthday = int(input("Enter the Month of your Birthday: "))
date_of_next_birthday = int(input("Enter the Date of your Birthday:"))
birthday = datetime.date(year_of_next_birthday, month_of_next_birthday, date_of_next_birthday)
today = datetime.date.today()
days_till_birthday = birthday - today
print(f"Number of Days till your next birthday are {days_till_birthday.days} days")