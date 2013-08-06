#!/usr/bin/python

import time

month_name = {'January': 'Morning Star',
              'February': "Sun's Dawn",
              'March': 'First Seed',
              'April': "Rain's Hand",
              'May': 'Second Seed',
              'June': 'Mid Year',
              'July': "Sun's Height",
              'August': 'Last Seed',
              'Suptember': 'Hearthfire',
              'October': 'Frostfall',
              'November': "Sun's Dusk",
              'December': 'Evening Star'}

weekday_name = {'Monday': 'Morndas',
                'Tuesday': 'Tirdas',
                'Wednesday': 'Middas',
                'Thursday': 'Turdas',
                'Friday': 'Fredas',
                'Saturday': 'Loredas',
                'Sunday': 'Sundas'}

def append_suffix(d):
    suffix = 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
    return str(d)+suffix

def convert_date(date=None):
    if date == None:
        date = time.strftime('%A %d %B').split()
    template = '{0}, {1} of {2}'
    print template.format(weekday_name[date[0]], 
        append_suffix(int(str(date[1]).lstrip('0'))), month_name[date[2]])


if __name__ == "__main__":
    convert_date()