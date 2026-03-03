from datetime import datetime, timedelta
import re

DATE_FORMAT = "%Y-%m-%d"


def _format_range(start: datetime, end: datetime):
    return {
        "start": start.strftime(DATE_FORMAT),
        "end": end.strftime(DATE_FORMAT),
    }


def _resolve_date_range(ent: str):
    """
    Resolve date range and return (start_datetime, end_datetime)
    without formatting.
    """
    ent = re.sub(r"^(the|for|during)\s+", "", ent)

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
        return target, target

    # --- Relative ranges ---
    if ent in ["last 7 days", "past 7 days"]:
        return today - timedelta(days=6), today

    if re.search(r"\b(last|previous)\s+week\b", ent):
        start = today - timedelta(days=today.weekday() + 7)
        end = start + timedelta(days=6)
        return start, end

    if ent == "this week":
        start = today - timedelta(days=today.weekday())
        return start, today

    if ent == "this month":
        start = today.replace(day=1)
        return start, today

    if ent in ["last month", "previous month"]:
        first_this_month = today.replace(day=1)
        last_month_end = first_this_month - timedelta(days=1)
        start = last_month_end.replace(day=1)
        return start, last_month_end

    if ent in ["last year", "previous year"]:
        last_year = today.year - 1
        start_last_year = datetime(last_year, 1, 1)
        end_last_year = datetime(last_year, 12, 31)
        return start_last_year, end_last_year

    # --- Dynamic pattern: last N days ---
    match = re.match(r"(last|past)\s+(\d+)\s+days?", ent)
    if match:
        n = int(match.group(2))
        return today - timedelta(days=n - 1), today

    return None


def extract_date_range(ent: str):
    """
    Extract and format date range.
    Returns formatted dict {start, end} or None.
    """
    resolved = _resolve_date_range(ent)

    if not resolved:
        return None

    start, end = resolved
    return _format_range(start, end)


def extract_comparison_date_range(ents: list):
    return {
        "time_period_1": extract_date_range(ents[0]),
        "time_period_2": extract_date_range(ents[1]),
    }
