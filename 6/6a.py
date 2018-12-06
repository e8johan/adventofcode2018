import re

class Location:    
    def __init__(self, id, text):
        m = re.match('^([0-9]+), ([0-9]+)$', text)
        self.x = int(m.group(1))
        self.y = int(m.group(2))
        self.id = id
        
    def distance_to(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

locations = []
next_id = 1

while True:
    try:
        l = Location(next_id, raw_input())
    except EOFError:
        break
    
    next_id += 1
    locations.append(l)

# determine size of field

min_x = locations[0].x
max_x = locations[0].x
min_y = locations[0].y
max_y = locations[0].y

for l in locations:
    if l.x < min_x:
        min_x = l.x
    if l.x > max_x:
        max_x = l.x
    if l.y < min_y:
        min_y = l.y
    if l.y > max_y:
        max_y = l.y

# determine distance to each coordinate
coords = []
for x in range(max_x-min_x):
    coords.append([])
    for y in range(max_y-min_y):
        distances = {}
        min_distance = max(max_x, max_y)
        for l in locations:
            d = l.distance_to(x+min_x, y+min_y)
            distances[l.id] = d
            if d < min_distance:
                min_distance = d
        closest = filter(lambda x : distances[x.id] == min_distance, locations)
        if len(closest) > 1:
            coords[x].append(-1)
        else:
            coords[x].append(closest[0].id)


# find id:s along the edges and add them to the blacklist, and -1 (i.e. undetermined)
blacklist = [-1]
for x in range(max_x-min_x):
    if coords[x][0] not in blacklist:
        blacklist.append(coords[x][0])
    if coords[x][max_y-min_y-1] not in blacklist:
        blacklist.append(coords[x][max_y-min_y-1])

for y in range(max_y-min_y):
    if coords[0][y] not in blacklist:
        blacklist.append(coords[0][y])
    if coords[max_x-min_x-1][y] not in blacklist:
        blacklist.append(coords[max_x-min_x-1][y])

# concatenate and filter coords
all_coords = []
for c in coords:
    all_coords = all_coords + filter(lambda x: x not in blacklist, c)

# determine frequence of each id    
freq_map = {}
for id in all_coords:
    if id in freq_map:
        freq_map[id] += 1
    else:
        freq_map[id] = 1

# find largest area
max_size = 0
for i, k in enumerate(freq_map):
    if freq_map[k] > max_size:
        max_size = freq_map[k]

print max_size
