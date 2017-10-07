from datetime import datetime

def convert_daynum_to_friendly(day_num):
    friendly_string = ""
    lastdigit = int(str(day_num[-1]))
    if lastdigit == 1 and day_num != 11:
         friendly_string = "st"
    
    if lastdigit == 2 and day_num != 12:
         friendly_string = "nd"
    
    if lastdigit == 3 and day_num != 13:
         friendly_string = "rd"

    else:
        friendly_string = "th"

    return "%s%s" % (day_num, friendly_string)

def get_time_now():
    time_now = datetime.now().time()
    time_hours = time_now.strftime("%I").lstrip('0')
    time_minutes = time_now.strftime("%M")
    ampm = time_now.strftime("%p").lower()

    return "%s:%s %s" % (time_hours, time_minutes, ampm)

def get_date_now():
    date_now = datetime.now()
    day = date_now.strftime("%A")
    day_number = convert_daynum_to_friendly(date_now.strftime("%d"))
    month_name = date_now.strftime("%B")

    formatted_date = "%s %s %s" % (day, day_number, month_name)

    return formatted_date

def get_now_zulu():
    date_now = datetime.now()
    zulu_date = "%sZ" % date_now.strftime("%Y-%m-%d")

    return zulu_date

def convert_zulu_to_dayname(day):
    dayname_from_zulu = datetime.strptime(day[:-1], "%Y-%m-%d").strftime("%a")

    return dayname_from_zulu