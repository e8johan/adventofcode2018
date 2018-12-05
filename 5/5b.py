polymer = raw_input()

def length(polymer):
    while True:
        found = False
        for i in range(len(polymer)-1):
            if not polymer[i] == polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
                polymer = polymer[:i] + polymer[i+2:]
                found = True
                break
        
        if not found:
            break

    return len(polymer)

alphabeth = "abcdefghijklmnopqrstuvwxyz"
polymers = {}
min_len = len(polymer)
for c in alphabeth:
    print c
    polymers[c] = filter(lambda x: not x.lower() == c, polymer)
    l = length(polymers[c])
    if l < min_len:
        min_len = l

print min_len
