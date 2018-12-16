world = []
mobs = []

def valid_coord(dss, y, x):
    if y >= 0 and y < len(dss):
        if x >= 0 and x < len(dss[y]):
            return True
    return False

class Mob:
    def __init__(self, x, y, is_elf):
        self.x = x
        self.y = y
        self.is_elf = is_elf
        self.health = 200
        
    def get_attacked(self):
        self.health -= 3
        if self.health <= 0:
            self.health = 0
        
    # order is important, reverse reading order
    neighbours = [ (0, -1), (-1, 0), (1, 0), (0, 1) ]
    
    def has_enemies(self):
        # Are there mobs of the other sort?
        active_mobs = filter(lambda m: m.health > 0, mobs)
        enemies = filter(lambda m: not m.is_elf == self.is_elf, active_mobs)
        
        if len(enemies) == 0:
            return False
        
        return True

    def act(self):
        # Find active mobs
        active_mobs = filter(lambda m: m.health > 0, mobs)
        enemies = filter(lambda m: not m.is_elf == self.is_elf, active_mobs)
        
        if len(enemies) == 0:
            return
        
        # Map up the world as -1 (wall) or -2 (space)
        distances = []
        for row in world:
            ds = []
            for col in row:
                if col == "#":
                    dist = -1
                else:
                    dist = -2
                ds.append(dist)
            distances.append(ds)

        # All mobs apart from self is marked as well
        for m in active_mobs:
            if not m == self:
                distances[m.y][m.x] = -1
        
        # For all enemies, map non-wall neighbours as zero (distance to enemy)
        for m in enemies:
            if not m.is_elf == self.is_elf:
                for nx, ny in Mob.neighbours:
                    cx = m.x+nx
                    cy = m.y+ny
                    if valid_coord(distances, cy, cx):
                        if distances[cy][cx] == -2:
                            distances[cy][cx] = 0

        # We are not next to an enemy, let's move towards one
        if not distances[self.y][self.x] == 0:
            updated = True
            while updated:
                updated = False
                for y in range(len(distances)):
                    for x in range(len(distances[y])):
                        if distances[y][x] >= 0:
                            found_path = False
                            for nx, ny in Mob.neighbours:
                                cx = x+nx
                                cy = y+ny
                                if valid_coord(distances, cy, cx):
                                    if distances[cy][cx] == -2 or distances[cy][cx] > distances[y][x]+1:
                                        distances[cy][cx] = distances[y][x]+1
                                        found_path = True
                                        updated = True

            #print "===>", self.x, self.y, self.is_elf
            #for ds in distances:
                #t = ""
                #for d in ds:
                    #t = t + " " + str(d)
                #print t

            tx = -1
            ty = -1
            best = -1
            for nx, ny in Mob.neighbours:
                if valid_coord(distances, self.y+ny, self.x+nx):
                    if distances[self.y+ny][self.x+nx] >= 0 and (best == -1 or distances[self.y+ny][self.x+nx] < best):
                        tx = self.x+nx
                        ty = self.y+ny
                        best = distances[self.y+ny][self.x+nx]
            
            # We have somewhere to move
            if not best == -1:
                self.x = tx
                self.y = ty
        
            # For all enemies, map non-wall neighbours as zero (distance to enemy) - updates if we are in range
            for m in enemies:
                if not m.is_elf == self.is_elf:
                    for nx, ny in Mob.neighbours:
                        cx = m.x+nx
                        cy = m.y+ny
                        if valid_coord(distances, cy, cx):
                            if distances[cy][cx] == -2:
                                distances[cy][cx] = 0

        # We are next to at least one enemy, attach the closest in reading order
        if distances[self.y][self.x] == 0:
            eligable = []
            for nx, ny in Mob.neighbours:
                for m in enemies:
                    if m.x == self.x+nx and m.y == self.y+ny:
                        eligable.append(m)
            eligable.sort(key=lambda m: (m.health, m.y, m.x))
            eligable[0].get_attacked()

# data structures and help functions
world = []
mobs = []
    
def print_world():
    for y in range(len(world)):
        r = ""
        ri = []
        for m in mobs:
            if m.y == y:
                t = ""
                if m.is_elf:
                    t = "E("
                else:
                    t = "G("
                t = t + str(m.health) + ")"
                ri.append(t)
        for x in range(len(world[y])):
            c = world[y][x]
            for m in mobs:
                if m.x == x and m.y == y:
                    if m.is_elf:
                        c = "E"
                    else:
                        c = "G"
            r = r+c
        print r + "   " + ", ".join(ri)

# read input
y = 0
while True:
    try:
        line = raw_input()
    except EOFError:
        break
    
    p = 0
    while True:
        p = line.find("E")
        if p > 0:
            mobs.append(Mob(p, y, True))
            line = line[:p] + "." + line[p+1:]
        else:
            break
    
    p = 0
    while True:
        p = line.find("G")
        if p > 0:
            mobs.append(Mob(p, y, False))
            line = line[:p] + "." + line[p+1:]
        else:
            break

    world.append(line)
    y += 1

# fight iteration
fighting = True
active_round = False
g = 0
while fighting:
#    print "Iteration:", g
#    print_world()
    mobs.sort(key=lambda m: (m.y, m.x))
    
    # has enemies?
    active_round = False
    for m in mobs:
        can_fight = m.has_enemies()
        fighting = fighting and can_fight
        active_round = active_round or can_fight
        if m.health > 0:
            m.act()
        
    mobs = filter(lambda m: m.health > 0, mobs)
    
    g += 1

g -= 1

print "Outcome"
print_world()

s = 0
for m in mobs:
    s += m.health
print "Result:", s*g, "(", s, "*", g, ")"
