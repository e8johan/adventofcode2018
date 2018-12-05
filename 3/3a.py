import re

class Tile:
    def __init__(self, text):
        m = re.match('^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$', text)
        self.id = int(m.group(1))
        self.x = int(m.group(2))
        self.y = int(m.group(3))
        self.w = int(m.group(4))
        self.h = int(m.group(5))

tiles = []

while True:
    try:
        t = Tile(raw_input())
    except EOFError:
        break
    
    tiles.append(t)

area = {}

for t in tiles:
    for x in range(t.x, t.x+t.w):
        for y in range(t.y, t.y+t.h):
            if x in area:
                if y in area[x]:
                    area[x][y] += 1
                else:
                    area[x][y] = 1
            else:
                area[x] = {}
                area[x][y] = 1

res = 0
for x, cols in enumerate(area):
    for xx, y in enumerate(area[x]):
        if area[x][y] > 1:
            res += 1
            
print(res)
