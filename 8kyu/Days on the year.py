def year_days(year):
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = f"{year} has 366 days"
    else:
        result = f"{year} has 365 days"

    return result