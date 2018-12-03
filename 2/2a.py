ids = []

while True:
    try:
        id = raw_input()
    except EOFError:
        break
    
    ids.append(id)

twos = 0
threes = 0

def appearances(char, string):
    res = 0
    
    pos = -1
    while True:
        try:
            pos = string.index(char, pos+1)
        except ValueError:
            break
        
        res += 1
    
    return res

for id in ids:
    found = {}
    for i,c in enumerate(id):
        apps = appearances(c, id)
        found[apps] = True

    if 2 in found:
        twos += 1
    if 3 in found:
        threes += 1

print twos*threes
