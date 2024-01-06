from datetime import datetime, timedelta
from typing import List


async def fetch_day_times():
    elem = datetime(
        hour=datetime.now().hour + 1 if datetime.now().minute > 30 else datetime.now().hour,
        minute=30 if datetime.now().minute < 30 else 0,
        second=0,
        day=datetime.now().day,
        month=datetime.now().month,
        year=datetime.now().year
    ).timestamp()
    day_time: List[float] = [elem]
    for i in range(49):
        elem += 1800
        day = datetime.utcfromtimestamp(elem)
        if day.hour >= 18 and day.minute > 0:
            elem = datetime(
                hour=9,
                minute=0,
                second=0,
                day=datetime.utcfromtimestamp(elem).day,
                month=datetime.utcfromtimestamp(elem).month,
                year=datetime.utcfromtimestamp(elem).year
            )
            elem += timedelta(days=1)
            elem = elem.timestamp()
        day_time.append(elem)
    return day_time
