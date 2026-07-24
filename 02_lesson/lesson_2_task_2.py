def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = 2028

print(f"Год {year}: {is_year_leap(year)}")
