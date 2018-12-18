world = []

while True:
    try:
        line = raw_input()
    except EOFError:
        break

    world.append(line)

def print_world():
    print "\n".join(world)

print "Initial state:"
print_world()

neighbours = [ (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1) ]

def is_valid(x, y):
    if x >= 0 and y >= 0:
        if y < len(world):
            if x < len(world[y]):
                return True
    return False

generation = 1
while generation <= 10:
    nextworld = []
    for y in xrange(len(world)):
        nextrow = []
        for x in xrange(len(world[y])):
            nextstate = world[y][x]
            
            opn = 0
            wod = 0
            yrd = 0
            for nx, ny in neighbours:
                if is_valid(x+nx, y+ny):
                    if world[y+ny][x+nx] == '.':
                        opn += 1
                    if world[y+ny][x+nx] == '|':
                        wod += 1
                    if world[y+ny][x+nx] == '#':
                        yrd += 1
            
            if world[y][x] == '.':
                # An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
                if wod >= 3:
                    nextstate = '|'
            elif world[y][x] == '|':
                # An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.
                if yrd >= 3:
                    nextstate = '#'
            elif world[y][x] == '#':
                # An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
                if not (yrd > 0 and wod > 0):
                    nextstate = '.'

            nextrow.append(nextstate)
        nextworld.append("".join(nextrow))
    
    world = nextworld
    print "After %s minutes:" % generation
    print_world()
    
    generation += 1

print sum(map(lambda x: x.count('|'), world)) * sum(map(lambda x: x.count('#'), world))
