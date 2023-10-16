from dateutil import parser


def validate(gt):
    """
    Validates a given time.
    gt = given time.
    """
    colonInd = gt.find(":")
    if colonInd != -1:
        colon = colonInd+1
        before = gt[1:colon]
        after = gt[colon:-1]
        if len(before) < 2 and len(after) > 4:
            raise ValueError("must be at least 2 values before colon and a maximum of 4 characters after colon.")
        elif len(after) == 0:
            raise ValueError("Must be value after colon.")
    elif len(gt) > 7:
        raise ValueError("Time is too long.")
    else:
        raise TypeError("must have a colon to be considered a valid time.")
    try:
        parser.parse(gt)
    except:
        raise TypeError("must be in parsable format")


def enterTime(msg="Enter a time"):
    """
    Gets time and parses it.
    """
    typing = True
    while typing:
        time = input(msg)
        try:
            validate(time)
        except:
            print("Please enter a valid time. \n \n Example: 8:30AM or 08:30")
        else:
            time = parser.parse(time)
            return f"{time.hour}:{time.minute}"
            typing = False