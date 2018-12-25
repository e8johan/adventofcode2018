import re

class Coord:
    def __init__(self, text):
        m = re.match('^([-]?[0-9]+),([-]?[0-9]+),([-]?[0-9]+),([-]?[0-9]+)$', text)
        self.c = [ int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)) ]
    
    def dist(self, c):
        sum = 0
        for i in xrange(4):
            sum += abs(c.c[i] - self.c[i])
        return sum
        

coords = []

while True:
    try:
        c = Coord(raw_input())
    except EOFError:
        break
    
    coords.append(c)

constellations = []
while len(coords):
    connected = [coords.pop()]

    while True:
        reached = []
        for c in coords:
            for k in connected:
                if k.dist(c) <= 3 and c not in reached:
                    reached.append(c)
        
        if len(reached) > 0:
            for r in reached:
                connected.append(r)
                coords.remove(r)
        else:
            break

    constellations.append(connected)

print len(constellations)
