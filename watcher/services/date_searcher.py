from datetime import date, timedelta

from watcher.services.argument_parser import allowed_days


def get_next_date_from_weekday(day_abbr: str):
    origin_date = date.today()
    days_offset = get_day_offset(origin_date.weekday(), allowed_days.index(day_abbr))

    return origin_date + timedelta(days_offset)


def get_day_offset(origin: int, target: int):
    return ((target - origin) + 7) % 7
