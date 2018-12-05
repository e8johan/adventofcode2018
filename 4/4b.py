import re

class Report:
    def __init__(self, text):
        m = re.match('^\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.*)$', text)
        self.year = int(m.group(1))
        self.month = int(m.group(2))
        self.day = int(m.group(3))
        self.hour = int(m.group(4))
        self.minute = int(m.group(5))
        
        if m.group(6) == 'falls asleep':
            self.action = 'sleep'
            self.no = -1
        elif m.group(6) == 'wakes up':
            self.action = 'wake'
            self.no = -1
        else:
            n = re.match('Guard #([0-9]+) begins shift', m.group(6))
            self.action = 'change'
            self.no = int(n.group(1))

    def before(self, r):
        if self.year > r.year:
            return False
        elif self.year < r.year:
            return True
        
        if self.month > r.month:
            return False
        elif self.month < r.month:
            return True
        
        if self.day > r.day:
            return False
        elif self.day < r.day:
            return True
        
        if self.hour > r.hour:
            return False
        elif self.hour < r.hour:
            return True
        
        if self.minute > r.minute:
            return False
        else:
            return True
    
    def __repr__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day) + " " + str(self.hour) + ":" + str(self.minute) + " " + self.action + " " + str(self.no)

reports = []

while True:
    try:
        r = Report(raw_input())
    except EOFError:
        break

    i = 0
    while i < len(reports) and reports[i].before(r):
        i += 1
    
    reports.insert(i, r)

# Put IDs on all reports
# Record all numbers (nos)
nos = []
no = -1
for r in reports:
    if r.action == 'change':
        no = r.no
    else:
        r.no = no
        
    if no > -1 and no not in nos:
        nos.append(no)

# Calculate number of sleep minutes per guard
# Calculate when each guard sleeps (sleep_map)
# Track maximum sleep and number (max_no)
sleep_map = {}
max_minutes = 0
max_no = -1
for no in nos:
    start_minute = 0
    sleep_map[no] = [0]*60
    for r in filter(lambda r: r.no == no, reports):
        if r.action == 'sleep':
            start_minute = r.minute
        elif r.action == 'wake':
            for m in range(start_minute, r.minute):
                sleep_map[no][m] += 1

    max_min = 0
    for m in sleep_map[no]:
        if m > max_min:
            max_min = m
    
    if max_min > max_minutes:
        max_minutes = max_min
        max_no = no

# Find minute with max sleep for guard
max_sleep = 0
max_minute = -1
for m, s in enumerate(sleep_map[max_no]):
    print m, s
    if s > max_sleep:
        max_sleep = s
        max_minute = m

print max_no, max_minute, max_no*max_minute
