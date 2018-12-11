grid_serial = int(input("Enter grid serial: "))

grid = []

for x in range(300):
    col = []
    for y in range(300):
        rack_id = x + 10
        fuel_level = (rack_id * y + grid_serial) * rack_id
        fuel_level = int(fuel_level/100) % 10 - 5
        col.append(fuel_level)
    grid.append(col)

maxres = -100
maxx = -1
maxy = -1
for x in range(300):
    col = []
    for y in range(300):
        if x+2 < 300 and y+2 < 300:
            res = 0
            for xx in range(3):
                for yy in range(3):
                    res += grid[x+xx][y+yy]
            if res > maxres:
                maxres = res
                maxx = x
                maxy = y

print maxx, maxy
