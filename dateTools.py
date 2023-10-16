from dateutil import parser
import datetime
import calendar


def validate(gd):
    """
    Checks whether date is valid.
    gd = date given.
    """
    try:
        gd = parser.parse(gd).strftime("%Y-%m-%d")
    except:
        raise TypeError("must be valid date.")
    else:
        gd = datetime.datetime.strptime(gd, "%Y-%m-%d")
        past = gd.month < datetime.datetime.now().month and gd.day < datetime.datetime.now().day
        if past == True:
            raise ValueError("date must not be past.")



def enterDate(msg="Enter date: "):
    """
    Gets dates as input. Parses and validates said date.
    """
    typing = True
    while typing:
        date = input(msg)
        try:
            validate(date)
        except TypeError:
            print("Please enter a date.")
        except ValueError:
            print(f"Date must be {calendar.month_name[datetime.date.today().month]} {datetime.date.today().day}, {datetime.date.today().year} or later")
        else:
            date = parser.parse(date)
            return f"{date.year}-{date.month}-{date.day}"
            typing = False



def minsBetween(a, b):
    """
    Gets the minutes between two datetime objects.
    """
    a = parser.parse(a)
    b = parser.parse(b)
    dif = a-b
    mins = dif.total_seconds()/60
    return int(mins)


