players = int(input("Number of players? "))
marbles = int(input("Last marble? "))

# Initialize game
playfield = [0]
current = 0
player = 0
marble = 0
points = [0] * players

while marble < marbles:
    marble += 1

    if marble % 23 == 0:
        points[player] += marble
        current -= 7
        while current < 0:
            current += len(playfield)
        points[player] += playfield.pop(current)
    else:
        target = current + 2
        if target > len(playfield):
            target -= len(playfield)
        playfield.insert(target, marble)
        current = target

    player += 1
    if player >= players:
        player = 0
        
print max(points)
