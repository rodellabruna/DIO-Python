from datetime import datetime, timezone, timedelta

d_oslo = datetime.now(timezone(timedelta(hours=2)))

d_sp = datetime.now(timezone(timedelta(hours=-3)))

print(d_oslo)
print(d_sp)
