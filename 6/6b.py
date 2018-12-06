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

# max possible radius + 1
radius = 10000 / len(locations) + 1

# determine distance to each coordinate and calculate size of area
area_size = 0
for x in range(max_x-min_x+2*radius):
    for y in range(max_y-min_y+2*radius):
        distance_sum = 0
        for l in locations:
            distance_sum += l.distance_to(x+min_x-radius, y+min_y-radius)
        if distance_sum < 10000:
            area_size += 1

print area_size
