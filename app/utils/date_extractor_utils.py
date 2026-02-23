from datetime import datetime, timedelta
import re

DATE_FORMAT = "%Y-%m-%d"


def _format_range(start: datetime, end: datetime):
    return {
        "start": start.strftime(DATE_FORMAT),
        "end": end.strftime(DATE_FORMAT),
    }


def extract_date_range(ent: str):
    """
    Extract a date range from a single DATE entity string.
    Returns dict {start, end} or None.
    """
    if not ent:
        return None

    ent = ent.lower().strip()
    today = datetime.today()

    # --- Single day cases ---
    single_day_map = {
        "today": 0,
        "yesterday": 1,
        "previous day": 1,
    }

    if ent in single_day_map:
        delta = single_day_map[ent]
        target = today - timedelta(days=delta)
        return _format_range(target, target)

    # --- Relative ranges ---
    if ent in ["last 7 days", "past 7 days"]:
        return _format_range(today - timedelta(days=6), today)

    if ent in ["last week", "previous week"]:
        start = today - timedelta(days=today.weekday() + 7)
        end = start + timedelta(days=6)
        return _format_range(start, end)

    if ent in ["this week"]:
        start = today - timedelta(days=today.weekday())
        return _format_range(start, today)

    if ent in ["this month"]:
        start = today.replace(day=1)
        return _format_range(start, today)

    if ent in ["last month", "previous month"]:
        first_this_month = today.replace(day=1)
        last_month_end = first_this_month - timedelta(days=1)
        start = last_month_end.replace(day=1)
        return _format_range(start, last_month_end)


    if ent in ["last year", "previous year"]:
        last_year = datetime.now().year - 1
        start_last_year = datetime(last_year, 1, 1)
        end_last_year = datetime(last_year, 12, 31)
        return _format_range(start_last_year, end_last_year)



    # --- Dynamic pattern: last N days ---
    match = re.match(r"(last|past)\s+(\d+)\s+days?", ent)
    if match:
        n = int(match.group(2))
        return _format_range(today - timedelta(days=n - 1), today)

    return None

