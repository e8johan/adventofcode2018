delta_list = []

while True:
    try:
        delta = int(raw_input())
    except ValueError:
        break
    except EOFError:
        break
    
    delta_list.append(delta)

known_freqs = []
freq = 0
i = 0
while True:
    freq += delta_list[i]
    
    i = i + 1
    if i >= len(delta_list):
        i = 0
        print freq
        
    if freq in known_freqs:
        break;
    
    known_freqs.append(freq)
    
print("Frequency: %s\n" % (freq))
