import re

class Pair:
    def __init__(self, text):
        m = re.match('^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$', text)
        self.name = m.group(1)
        self.before = m.group(2)

pairs = []

while True:
    try:
        p = Pair(raw_input())
    except EOFError:
        break
    
    pairs.append(p)

blocked_by = {}
for p in pairs:
    if p.name not in blocked_by:
        blocked_by[p.name] = []
    
    if p.before in blocked_by:
        blocked_by[p.before].append(p.name)
    else:
        blocked_by[p.before] = [p.name]

order = ""
while True:
    available = []
    for i, k in enumerate(blocked_by):
        if len(blocked_by[k]) == 0:
            available.append(k)
    available.sort()
    for n in available:
        order += n
        del blocked_by[n]
        for i, k in enumerate(blocked_by):
            blocked_by[k] = filter(lambda x: not x == n, blocked_by[k])
    if len(blocked_by) == 0:
        break
    if len(available) == 0:
        raise Exception("No valid path available - current order " + order)

print order
