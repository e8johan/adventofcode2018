players = int(input("Number of players? "))
marbles = int(input("Last marble? "))

class Node:
    def __init__(self, v, n=None, p=None):
        self.v = v
        self.n = n
        self.p = p

# Initialize game
current = Node(0)
current.n = current
current.p = current

player = 0
marble = 0
points = [0] * players

while marble < marbles:
    marble += 1

    if marble % 23 == 0:
        for i in range(7):
            current = current.p
        points[player] += marble + current.v
        current.p.n = current.n
        current.n.p = current.p
        current = current.n
    else:
        for i in range(1):
            current = current.n        
        new_marble = Node(marble, current.n, current)
        current.n.p = new_marble
        current.n = new_marble
        current = new_marble
        
    player += 1
    if player >= players:
        player = 0
        
print max(points)
