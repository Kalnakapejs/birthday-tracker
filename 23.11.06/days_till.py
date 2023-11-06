from datetime import datetime
days_in = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
def is_leap(year: int) -> bool:
    """Every year that is exactly divisable by four is a leap year, except for years that are exactly divisable by 100"""
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
    
def days_till(month: int,day: int) -> int:
    """
    Returns the number of days till the next day of the month, for example, 7th of july\n
    Arguments: \n
    Month - integer from 1 to 12 (January to December)\n
    Day - integer from 1 to 31 (day of the month)\n
    """
    c_day = datetime.now().day
    #current day
    c_month = datetime.now().month
    #current month
    c_year = datetime.now().year
    #current year
    result = 0
    while c_month != month or c_day != day:
        c_day +=1
        result +=1
        c_month_days = days_in[c_month]
        if c_month == 2 and is_leap(c_year):
            c_month_days = 29
        if c_day > c_month_days:
            c_month +=1
            c_day = 1
        if c_month > 12:
            c_month = 1 
            c_day = 1
            c_year =+ 1
    return result