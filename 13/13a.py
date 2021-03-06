class Cart:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.next_turn_state = 0
        self.direction = d
    
    def move(self, tracks):
        if self.direction == "<":
            self.x -= 1
        elif self.direction == ">":
            self.x += 1
        elif self.direction == "^":
            self.y -= 1
        elif self.direction == "v":
            self.y += 1
            
        t = tracks[self.y][self.x]
        
        if t == "/":
            if self.direction == "<":
                self.direction = "v"
            elif self.direction == ">":
                self.direction = "^"
            elif self.direction == "^":
                self.direction = ">"
            elif self.direction == "v":
                self.direction = "<"
        elif t == "\\":
            if self.direction == "<":
                self.direction = "^"
            elif self.direction == ">":
                self.direction = "v"
            elif self.direction == "^":
                self.direction = "<"
            elif self.direction == "v":
                self.direction = ">"
        elif t == "+":
            if self.next_turn_state == 0:
                # left
                if self.direction == "<":
                    self.direction = "v"
                elif self.direction == ">":
                    self.direction = "^"
                elif self.direction == "^":
                    self.direction = "<"
                elif self.direction == "v":
                    self.direction = ">"

                self.next_turn_state = 1
            elif self.next_turn_state == 1:
                # straight
                self.next_turn_state = 2
            elif self.next_turn_state == 2:
                # right
                if self.direction == "<":
                    self.direction = "^"
                elif self.direction == ">":
                    self.direction = "v"
                elif self.direction == "^":
                    self.direction = ">"
                elif self.direction == "v":
                    self.direction = "<"

                self.next_turn_state = 0

tracks = []
carts = []
y = 0

while True:
    try:
        text = raw_input()
    except EOFError:
        break

    p = 0
    while True:
        p = text.find("<")
        if p > 0:
            carts.append(Cart(p, y, '<'))
            text = text[:p] + "-" + text[p+1:]
        else:
            break

    p = 0
    while True:
        p = text.find(">")
        if p > 0:
            carts.append(Cart(p, y, '>'))
            text = text[:p] + "-" + text[p+1:]
        else:
            break

    p = 0
    while True:
        p = text.find("v")
        if p > 0:
            carts.append(Cart(p, y, 'v'))
            text = text[:p] + "|" + text[p+1:]
        else:
            break

    p = 0
    while True:
        p = text.find("^")
        if p > 0:
            carts.append(Cart(p, y, '^'))
            text = text[:p] + "|" + text[p+1:]
        else:
            break

    tracks.append(text)
    y += 1
    
crashed = False
while not crashed:
    carts.sort(key=lambda c: (c.x, c.y))

    for c in carts:
        c.move(tracks)
        for k in carts:
            if not c == k and c.x == k.x and c.y == k.y:
                print "Collision at", c.x, c.y
                crashed = True
