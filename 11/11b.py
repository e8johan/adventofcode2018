grid_serial = int(input("Enter grid serial: "))

grid_size = 300
grid = []

for x in range(grid_size):
    col = []
    for y in range(grid_size):
        rack_id = x + 10
        fuel_level = (rack_id * y + grid_serial) * rack_id
        fuel_level = int(fuel_level/100) % 10 - 5
        col.append(fuel_level)
    grid.append(col)

maxres = -100
maxx = -1
maxy = -1
maxsize = -1

for s in range(1,300):
    col = []
    for y in range(grid_size):
        res = 0
        for x in range(s):
            res += grid[x][y]
        col.append(res)

    for x in range(grid_size-s):
        for y in range(grid_size-s-1):
            res = 0
            for yy in range(s):
                res += col[y+yy]
            if res > maxres:
                maxres = res
                maxx = x
                maxy = y
                maxsize = s
        
        for y in range(grid_size):
            col[y] = col[y] - grid[x][y] + grid[x+s][y]

print maxx, maxy, maxsize
