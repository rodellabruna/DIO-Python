#pip install pytz

from datetime import datetime
import pytz

d = datetime.now(pytz.timezone("Europe/Oslo"))
d2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)
print(d2)