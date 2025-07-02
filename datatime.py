from datetime import datetime,timedelta

# Date and time class

# Now Methods
current_date = datetime.now() # Current date and time
print(current_date.day) # Day
print(current_date.month) # Month
print(current_date.year) # Year
print(current_date.today()) # Today


# Format date
formatted_date = current_date.strftime('%d/%m/%Y, %H:%M:%S')
print(formatted_date)

# Parse date
parsed_date = datetime.strftime(current_date, '%d/%m/%Y, %H:%M:%S')
print(parsed_date)

# Time delta (Difference between two dates)
future_date = current_date + timedelta(days=2)
print(future_date)

past_date = current_date - timedelta(days=3)
print(past_date)

# Time Stamp
timestamp = current_date.timestamp()
print(timestamp)

# From timestamp
from_timestamp = datetime.fromtimestamp(timestamp)
print(from_timestamp)

print("Some changes")

thirty_days = timedelta(days=30)
date_thirty_days = current_date + thirty_days

ten_days = timedelta(days=10)
date_ten_days = current_date + ten_days

print(date_thirty_days > date_ten_days)


import time
timestamp = int(time.time())  # Current Unix timestamp (seconds)
print(datetime.fromtimestamp(timestamp))  # Convert the timestamp to datetime
