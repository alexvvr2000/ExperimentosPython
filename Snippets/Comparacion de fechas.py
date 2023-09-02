from datetime import date, timedelta

today: date = date.today()
past: date = today - timedelta(days=365)
future: date = today + timedelta(days=365)

print(past)
print(future)

print(future >= today)
print(today >= future)
print(past >= today)
print(today >= past)
