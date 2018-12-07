polymer = raw_input()

i=0
while i < len(polymer)-1:
    if not polymer[i] == polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
        polymer = polymer[:i] + polymer[i+2:]
        if i > 0:
            i -= 1
    else:
        i += 1

print len(polymer)
