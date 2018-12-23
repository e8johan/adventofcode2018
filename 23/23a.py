import re

class Bot:
    def __init__(self, text):
        m = re.match('^pos=<([-]?[0-9]+),([-]?[0-9]+),([-]?[0-9]+)>, r=([0-9]+)$', text)
        self.x = int(m.group(1))
        self.y = int(m.group(2))
        self.z = int(m.group(3))
        self.r = int(m.group(4))
        
    def reaches(self, x, y, z):
        if abs(x-self.x)+abs(y-self.y)+abs(z-self.z) <= self.r:
            return True
        else:
            return False

def findstrongest(bs):
    if len(bs) == 0:
        return -1
    
    maxr = bs[0].r
    maxi = 0
    for i in xrange(0, len(bs)):
        b = bs[i]
        if b.r > maxr:
            maxr = b.r
            maxi = i
    
    return maxi

def findsinglereach(bs, i):
    reaches = []
    b = bs[i]
        
    for j in xrange(0, len(bs)):
        bb = bs[j]
        if b.reaches(bb.x, bb.y, bb.z):
            reaches.append(j)
                
    return len(reaches)

def findreach(bs, i):
    visited = []
    tovisit = [i]
    
    while len(tovisit) > 0:
        ii = tovisit.pop()
        visited.append(ii)
        b = bs[ii]
        
        print "==>", ii
        
        for j in xrange(0, len(bs)):
            if j not in visited:
                bb = bs[j]
                if b.reaches(bb.x, bb.y, bb.z):
                    tovisit.append(j)
                    print "   ", j
    
    return len(visited)

bots = []

while True:
    try:
        b = Bot(raw_input())
    except EOFError:
        break
    
    bots.append(b)

print "Part 1:", findsinglereach(bots, findstrongest(bots))
