def getDays(hours, day_change):
    if day_change == 1:
        return int(hours/24) + 1, hours % 12
    return int(hours/24), hours % 12


def add_time(start, duration, today=None):
    # Initialisation of  variables
    day = ['monday', 'tuesday', 'wednesday',
           'thursday', 'friday', 'saturday', 'sunday']
    meridiems = ['AM', 'PM']
    new_time = ''
    new_time_hr = 0
    new_time_mins = 0
    new_day = 0
    days_later = ''

    # Breaking down the Start Time
    start_time, start_mer = start.split()[0], start.split()[1]
    start_hr, start_mins = int(start_time.split(
        ':')[0]), int(start_time.split(':')[1])

    # Breaking down the Duration Time
    dur_hr, dur_mins = int(duration.split(":")[0]), int(duration.split(":")[1])

    # Adding up the mins and carry hours
    total_mins = start_mins + dur_mins
    new_time_hr, new_time_mins = int(total_mins/60), total_mins % 60
    new_time_hr += start_hr + dur_hr

    # Calculating the new meredium and if day changed or no
    new_mer = meridiems[(meridiems.index(start_mer) +
                         int(new_time_hr / 12)) % 2]
    day_change = meridiems.index(start_mer) - meridiems.index(new_mer)

    # Calculating days
    new_day, new_time_hr = getDays(new_time_hr, day_change)

    # Adjusting the midnight and noon
    if new_time_hr == 0:
        new_time_hr = 12

    # Condition for same day AM -> AM or AM -> PM
    if new_day == 0 or day_change == -1:
        days_later = ''

    # Condition for Next day and if its PM -> AM or PM -> PM
    elif new_day == 1 and (day_change == 1 or day_change == 0):
        days_later = ' (next day)'

    # Condition for more than 1 day
    else:
        days_later = " (" + str(new_day) + " days later)"

    if today:
        new_day = day[(day.index(today.lower()) + new_day) % 7]
        new_time = str(new_time_hr) + ":" + str(new_time_mins).rjust(2,
                                                                     '0') + " " + new_mer + ", " + new_day.capitalize() + days_later
        return new_time

    new_time = str(new_time_hr) + ":" + \
        str(new_time_mins).rjust(2, '0') + " " + new_mer + days_later
    return new_time
