import vobject
import csv
import requests

class Calendar():
    def __init__(self, link):
        #a calendar is a list of events
        self.cal = []
        r = requests.get(link)
        decoded_events = r.content.decode("utf-8").split("\n")


class Event():
    def __init__(self, ):
        'BEGIN:VEVENT\r', 'DTSTART;TZID=Asia/Manila:20230922T130000\r', 'DTEND;TZID=Asia/Manila:20230922T143000\r', 'DTSTAMP:20250218T124103Z\r', 'UID:5uq08lf4sv9afu2boa7893305m@google.com\r', 'RECURRENCE-ID;TZID=Asia/Manila:20230922T130000\r', 'CREATED:20230908T140514Z\r', 'LAST-MODIFIED:20240119T015938Z\r', 'SEQUENCE:0\r', 'STATUS:CONFIRMED\r', 'SUMMARY:KAS 1 WFW1 - asynch\r', 'TRANSP:OPAQUE\r', 'END:VEVENT\r'

# "https://calendar.google.com/calendar/ical/3q8fom4rgsrc69lnrsths0d1jg%40group.calendar.google.com/private-c54511e0a53a418854721c0deccdce26/basic.ics

with open('sample.csv', mode='w') as csv_out:
    csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['WHAT', 'WHO', 'FROM', 'TO', 'DESCRIPTION'])

    # read the data from the file
    data = open("calendar/basic.ics").read()
    # print(data)

    # iterate through the contents
    for cal in vobject.readComponents(data):
        for component in cal.components():
            if component.name == "VEVENT":
                # print(component)
                # break
                # write to csv
                csv_writer.writerow([component.summary.valueRepr()," ",component.dtstart.valueRepr(),component.dtend.valueRepr()," "])