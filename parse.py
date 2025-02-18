import vobject
import csv
import requests

class Calendar():
    def __init__(self, link):
        #a calendar is a list of events
        self.cal = []
        r = requests.get(link)
        decoded_events = r.content.decode("utf-8").split("\n")

        cur = {}
        event_info_start = False
        for s in decoded_events:
            if s == "BEGIN:VEVENT\r":
                event_info_start = True
            elif s == "END:VEVENT\r":
                event_info_start = False
                if len(cur) > 0:
                    self.cal.append(Event(cur))
            elif len(s.split(":")) > 1:
                cur[s.split(":")[0]] = s.split(":")[1]                

    def check(self):
        for i in self.cal:
            print(i.event)
            print("---")

class Event():
    def __init__(self, event):
        self.event = event
    

# "https://calendar.google.com/calendar/ical/3q8fom4rgsrc69lnrsths0d1jg%40group.calendar.google.com/private-c54511e0a53a418854721c0deccdce26/basic.ics

def main():
    google_calendar = Calendar("https://calendar.google.com/calendar/ical/3q8fom4rgsrc69lnrsths0d1jg%40group.calendar.google.com/private-c54511e0a53a418854721c0deccdce26/basic.ics")
    google_calendar.check()


if __name__ == "__main__":
    main()