def countDays(years, month):
    days = ((years*12)+month)*29
    print(f'There are {days} days in {years} years and {month} month')

countDays(4, 6)