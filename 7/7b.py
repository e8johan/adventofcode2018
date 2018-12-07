import re

class Pair:
    def __init__(self, text):
        m = re.match('^Step ([A-Z]) must be finished before step ([A-Z]) can begin\.$', text)
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

no_of_workers = 5

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
workers = ['.'] * no_of_workers
worker_time = [0] * no_of_workers
time_spent = 0
while True:
    # Find next task(s)
    available = []
    for i, k in enumerate(blocked_by):
        if len(blocked_by[k]) == 0:
            available.append(k)

    if len(available) == 0:
        raise Exception("No valid path available - current order " + order)

    # ongoing tasks are not available
    available = filter(lambda x: x not in workers, available)
    available.sort()
    
    # assign idle workers
    for i in range(no_of_workers):
        if workers[i] == '.' and len(available) > 0:
            workers[i] = available[0]
            worker_time[i] = alphabet.find(available[0])+61
            available = available[1:]

    # iterate until at least one task is done
    finished = False
    while not finished:
        time_spent += 1
        for i in range(no_of_workers):
            if workers[i] != '.':
                worker_time[i] -= 1
                                        
        for i in range(no_of_workers):
            if worker_time[i] == 0 and not workers[i] == '.':
                del blocked_by[workers[i]]
                for j, k in enumerate(blocked_by):
                    blocked_by[k] = filter(lambda x: not x == workers[i], blocked_by[k])
                workers[i] = '.'
                finished = True
                
    if len(blocked_by) == 0:
        break

print time_spent
