def leapyear(year):
    if (year % 4) == 0:
        return "leap year"
        if (year % 100) == 0:
            return "leap year"
            if (year % 400) == 0:
                return "leap year"
            else:
                return "not leap year"
        else:
            return "leap year"
    else:
        return "not leap year"
