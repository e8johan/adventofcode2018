import re

class Coord:
    def __init__(self, text):
        m = re.match("^position\=\<[\s]*([0-9\-]+),[\s]*([0-9\-]+)\> velocity\=\<[\s]*([0-9\-]+),[\s]*([0-9\-]+)\>$", text)
        self.x = int(m.group(1))
        self.y = int(m.group(2))
        self.dx = int(m.group(3))
        self.dy = int(m.group(4))
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
    def unupdate(self):
        self.x -= self.dx
        self.y -= self.dy

def randomness(cs):
    xs = []
    ys = []
    
    for c in cs:
        if c.x not in xs:
            xs.append(c.x)
        if c.y not in ys:
            ys.append(c.y)
    
    return len(xs) + len(ys)

def message(cs):
    minx = cs[0].x
    miny = cs[0].y
    maxx = minx
    maxy = miny
    
    for c in cs:
        if c.x > maxx:
            maxx = c.x
        if c.x < minx:
            minx = c.x
        if c.y > maxy:
            maxy = c.y
        if c.y < miny:
            miny = c.y
    
    rows = []
    for r in range(maxy - miny+1):
        rows.append(["."] * (maxx - minx+1))
    for c in cs:
        rows[c.y-miny][c.x-minx] = "#"
        
    for r in rows:
        print "".join(r)
        
coords = []

while True:
    try:
        c = Coord(raw_input())
    except EOFError:
        break
    
    coords.append(c)

lastrandomness = randomness(coords)
i = 0
while True:
    r = randomness(coords)
    
    if r > lastrandomness and r < 100: # This 100 is to ensure that we hit the global minimum
        for c in coords:
            c.unupdate()        
        i = i-1
        break
    lastrandomness = r

    i += 1
    for c in coords:
        c.update()

message(coords)
print i
