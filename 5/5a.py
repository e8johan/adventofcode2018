polymer = raw_input()

while True:
    found = False
    for i in range(len(polymer)-1):
        if not polymer[i] == polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
            polymer = polymer[:i] + polymer[i+2:]
            found = True
            break
    
    if not found:
        break

print len(polymer)
