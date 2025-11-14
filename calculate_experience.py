import datetime

start_year, start_month = 2019, 12
now = datetime.datetime.utcnow()
months = (now.year - start_year)*12 + (now.month - start_month)
years = months // 12 + (1 if months % 12 > 0 else 0)
print(years)
