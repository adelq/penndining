from datetime import datetime, time

class hall():
    """
    Creates new objects with open and closing times
    """
    def __init__(self, open, close):
        self.open = open
        self.close = close

class hours():
    """
    Creates object for eating time with opening and closing times
    """
    def __init__(self, open, close):
        self.open = open
        self.close = close

def is_open(hall):
    """
    Returns boolean of whether dining hall is currently open or closed
    """
    current = datetime.now()
    ctm = current.time()
    if current.weekday() == 4:
        if ctm > time(11) and ctm < time(14):
            print("Lunch")
        elif ctm > time(17) and ctm < time(19,30):
            print("Dinner")
        else:
            print("Closed")
    elif current.weekday() == 5:
        if ctm > time(11) and ctm < time(15):
            print("Brunch")
        elif ctm > time(17) and ctm < time(19):
            print("Dinner")
        else:
            print("Closed")
    elif current.weekday() == 6:
        if ctm > time(11) and ctm < time(15):
            print("Brunch")
        elif ctm > time(17) and ctm < time(20):
            print("Dinner")
        else:
            print("Closed")
    else:
        if ctm > time(11) and ctm < time(14):
            print("Lunch")
        elif ctm > time(17) and ctm < time(21):
            print("Dinner")
        else:
            print("Closed")

def time_to_close(hall):
    """
    Returns number of hours until dining hall closed
    Returns -1 if is closed already
    """
    status = is_open(hall)
    if status == "Closed":
        return -1
    else:
        current = datetime.now()
        ctm = current.time()
        wd = current.weekday()
        if wd == 4:
            if status == "Lunch":
                return time(14) - ctm
            else:
                return time(19,30) - ctm
        if wd == 5:
            if status == "Brunch":
                return time(15) - ctm
            else:
                return time(19) - ctm
        if wd == 6:
            if status == "Brunch":
                return time(15) - ctm
            else:
                return time(20) - ctm
        else:
            if status == "Lunch":
                return time(14) - ctm
            else:
                return time(21) - ctm

def status(hall):
    if not open(hall) or time_to_close(hall) == -1:
        return "Closed"
    elif time_to_close(hall) < 30:
        return "Closing"
    else:
        return "Open"

time_to_close("commons")
