import re

coords = []

while True:
    try:
        line = raw_input()
    except EOFError:
        break

    m = re.match("^([xy])=([0-9]+), ([xy])=([0-9]+)..([0-9]+)$", line)
    
    if m.group(1) == "x":
        for y in range(int(m.group(4)), int(m.group(5))+1):
            coords.append((int(m.group(2)), y))
    else:
        for x in range(int(m.group(4)), int(m.group(5))+1):
            coords.append((x, int(m.group(2))))

minx = 500
maxx = 500
miny = 0
realminy = 1000
maxy = 0

for x, y in coords:
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if y < realminy:
        realminy = y
    if y > maxy:
        maxy = y

minx -=1
maxx +=1

world = []

for y in range(miny, maxy+2):
    row = ['X'] + ['.']*(maxx-minx+1) + ['X']
    for xx, yy in coords:
        if yy == y:
            row[xx-minx+1] = '#'
    
    if y == 0:
        row[500-minx+1] = '+'

    world.append("".join(row))

def fillwater(x,y):
    visited = []
    tovisit = [(x,y)]
    while len(tovisit) > 0:
        xx, yy = tovisit.pop()
        
        if yy > maxy:
            continue
        
        visited.append((xx, yy))
    
        if world[yy+1][xx] == '.':
            if (xx, yy+1) not in visited:
                tovisit.append((xx, yy+1))
        else:
            res = False
            if world[yy][xx-1] == '.':
                if (xx-1, yy) not in visited:
                    tovisit.append((xx-1, yy))
            if world[yy][xx+1] == '.':
                if (xx+1, yy) not in visited:
                    tovisit.append((xx+1, yy))

            row = map(lambda r: r[0], filter(lambda r: r[1] == yy, visited))
            row.sort()

            spans = []
            lastx = row.pop(0)
            startx = lastx
            while len(row) > 0:
                xxx = row.pop(0)
                if not lastx+1 == xxx:
                    spans.append((startx, lastx))
                    startx = xxx
                lastx = xxx
            spans.append((startx, lastx))

            spans = filter(lambda s: s[0] <= xx and s[1] >= xx, spans)
            span = spans[0]
            if (not world[yy][span[0]-1] == '.') and (not world[yy][span[1]+1] == '.'):
                world[yy] = world[yy][:span[0]] + '~' * (span[1] - span[0] + 1) + world[yy][span[1]+1:]
                entries = filter(lambda v: v[1] == yy-1 and v[0] >= span[0] and v[0] <= span[1], visited)
                tovisit = tovisit + entries
                visited = filter(lambda v: v not in entries, visited)

    for xx, yy in visited:
        if world[yy][xx] == '.':
            world[yy] = world[yy][:xx] + '|' + world[yy][xx+1:]

    return len(filter(lambda v: v[1]>= realminy, visited))

print "Part one:", fillwater(500-minx+1,0)
print "Part two:", sum(map(lambda r: r.count('~'), world))
