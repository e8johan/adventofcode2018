ids = []

while True:
    try:
        id = raw_input()
    except EOFError:
        break
    
    ids.append(id)


def differences(a, b):
    res_count = 0
    res_text = ""
    
    for i,c in enumerate(a):
        if not b[i] == c:
            res_count += 1
        else:
            res_text += c
    
    return res_count, res_text
    
i = 0
while i < len(ids):
    j = i+1
    while j < len(ids):
        count, text = differences(ids[i], ids[j])
        if count == 1:
            print text
            i = len(ids)
            j = len(ids)
            
        j += 1
        
    i += 1
