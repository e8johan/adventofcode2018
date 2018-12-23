rooms = {}
neighbours = { 'E': (1, 0), 'W': (-1, 0), 'N': (0, -1), 'S': (0, 1) }
opposite = { 'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N' }

def buildmap(x, y, e):
    startx = x
    starty = y
    i = 0
    
    branchcount = 0
    branchstart = -1
    
    while i < len(e):
        if e[i] == '|':
            if branchstart == -1:
                x = startx
                y = starty
        elif e[i] == '(':
            if branchstart == -1:
                branchstart = i
            branchcount += 1
        elif e[i] == ')':
            branchcount -= 1
            if branchcount == 0:
                buildmap(x, y, e[branchstart+1:i])
                branchstart = -1
        else:
            if branchstart == -1:
                # build the map
                if (x,y) in rooms:
                    if e[i] not in rooms[(x,y)]:
                        rooms[(x,y)].append(e[i])
                else:
                    rooms[(x,y)] = [e[i]]

                x += neighbours[e[i]][0]
                y += neighbours[e[i]][1]

                if (x,y) in rooms:
                    if e[i] not in rooms[(x,y)]:
                        rooms[(x,y)].append(opposite[e[i]])
                else:
                    rooms[(x,y)] = [opposite[e[i]]]
            
        i += 1
        
def printmap():
    coords = rooms.keys()
    if len(coords) == 0:
        return
    
    minx = coords[0][0]
    miny = coords[0][1]
    maxx = minx
    maxy = miny
    
    for c in coords:
        if c[0] < minx:
            minx = c[0]
        if c[0] > maxx:
            maxx = c[0]
        if c[1] < miny:
            miny = c[1]
        if c[1] > maxy:
            maxy = c[1]
    
    for y in xrange(miny, maxy+1):
        if y == miny:
            print "".join(["#"] * ((maxx-minx)*2+3))
        midrow = "#"
        botrow = "#"
        for x in xrange(minx, maxx+1):
            if (x,y) in rooms:
                midrow += " "
                r = rooms[(x,y)]
                if 'E' in r:
                    midrow += "|"
                else:
                    midrow += "#"
                if 'S' in r:
                    botrow += "-"
                else:
                    botrow += "#"
                botrow += "#"
            else:
                midrow += "##"
                botrow += "##"
        print midrow
        print botrow

def maxdistance():
    dists = {}
    
    visited = []
    tovisit = [(0, 0, 0)]
    while len(tovisit) > 0:
        x, y, c = tovisit.pop(0)
        
        if (x,y) in dists:
            if c < dists[(x,y)]:
                dists[(x,y)] = c
            else:
                continue
        else:
            dists[(x,y)] = c

        if (x,y) in rooms:
            for d in rooms[(x,y)]:
                tovisit.append((x+neighbours[d][0], y+neighbours[d][1], c+1))
    
    print "Part 1:", max(dists.values())
    print "Part 2:", sum(map(lambda x: 1 if x>=1000 else 0, dists.values()))

expr = raw_input("input: ")

if expr[0] == '^' and expr[-1] == '$':
    expr = expr[1:-1]
else:
    print "Invalid input!"
    exit()

buildmap(0, 0, expr)
#printmap()
maxdistance()
