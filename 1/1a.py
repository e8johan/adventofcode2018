freq = 0

while True:
    try:
        delta = int(raw_input())
    except ValueError:
        break
    except EOFError:
        break
    
    freq += delta
    
print("Frequency: %s\n" % (freq))
