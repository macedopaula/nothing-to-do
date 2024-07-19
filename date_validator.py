def date_validator(year, month, day):
    if year < 0:
        raise Exception(f'Invalid date. Year can not be negative')
    elif (year % 4 == 0):
        if month == 2:
            if (day < 0 or day > 29):
                raise Exception(f'Invalid date. February has 29 days')
        elif month < 8 and month > 0:
            if month %2 == 0 and (day < 0 or day > 30):
                raise Exception(f'Invalid date. Month {month} has 30 days.')
            elif month %2 == 1 and (day < 0 or day > 31):
                raise Exception(f'Invalid date. Month {month} has 31 days.')
        elif month > 8 and month < 13:
            if month %2 == 1 and (day < 0 or day > 30):
                raise Exception(f'Invalid date. Month {month} has 30 days.')
            elif month %2 == 0 and (day < 0 or day > 31):
                raise Exception(f'Invalid date. Month {month} has 31 days.')
        else:
            raise Exception(f'Month should be a number from 1 to 12.')
    else:
        if month == 2: 
            if (day < 0 or day > 28):
                raise Exception(f'Invalid date. February has 28 days')
        elif month < 8 and month > 0:
            if month %2 == 0 and (day < 0 or day > 30):
                raise Exception(f'Invalid date. Month {month} has 30 days.')
            elif month %2 == 1 and (day < 0 or day > 31):
                raise Exception(f'Invalid date. Month {month} has 31 days.')
        elif month > 8 and month < 13:
            if month %2 == 1 and (day < 0 or day > 30):
                raise Exception(f'Invalid date. Month {month} has 30 days.')
            elif month %2 == 0 and (day < 0 or day > 31):
                raise Exception(f'Invalid date. Month {month} has 31 days.')
        else:
            raise Exception(f'Month should be a number from 1 to 12.')

        
if __name__ == "__main__":
    date_validator(year, month, day)