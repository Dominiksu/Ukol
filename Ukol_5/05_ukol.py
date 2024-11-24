import datetime
from dateutil.relativedelta import relativedelta

def append_date(day_format):
    with open ("Ukoly/Ukol_5/05_text",mode="a", encoding="utf-8") as file:
        file.write(day_format)


def loop_date():
    d = datetime.date(2024, 1, 1)
    for number in range(12):
        raw_date = d + relativedelta(months = number)
        day_format = raw_date.strftime("%d/%m/%y\n")
        append_date(day_format)

loop_date()