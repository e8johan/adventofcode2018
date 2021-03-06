import re

class State:
    def __init__(self, state, offset):
        if type(state) is str:
            self.state = []
            for c in state:
                self.state.append(c)
        else:
            self.state = state
            
        self.offset = offset
        
    def next(self, rules):
        next_state = []
        next_offset = self.offset-2
        
        for i in range(next_offset, self.offset + len(self.state)+2):
            key = ""
            if i < self.offset+2:
                key = "".join(self.state[:i-self.offset+3])
                key = "".join(['.']*(5-len(key))) + key
            elif i > self.offset + len(self.state)-3:
                key = "".join(self.state[i-self.offset-2:])
                key = key + "".join(['.']*(5-len(key)))
            else:
                key = "".join(self.state[i-self.offset-2:i-self.offset+3])
            
            if key in rules:
                next_state.append(rules[key])
            else:
                next_state.append('.')
        
        # trim '.' and update offset
        while next_state[0] == '.':
            del next_state[0]
            next_offset += 1
            
        # trim '.' from the other end
        while next_state[-1] == '.':
            del next_state[-1]

        return State(next_state, next_offset)

    def sum(self):
        res = 0
        value = self.offset
        for c in self.state:
            if c == '#':
                res += value
            value += 1
        return res

rules = {}
s = State(re.match("^initial state: ([\.#]+)$", raw_input()).group(1), 0)

while True:
    try:
        text = raw_input()
        if text == "":
            continue
        else:
            m = re.match("^([\.#]+) => ([\.#]+)$", text)
            if m.group(2) == "#":
                rules[m.group(1)] = m.group(2)
    except EOFError:
        break

last = ""
lo = 0
i = 0
while True:
    this = "".join(s.state)
    print i, this, s.offset, s.sum()
    i += 1
    if last == this and s.offset == lo or i > 120:
        break
    last = this
    lo = s.offset
    s = s.next(rules)
    
# pattern seen, s.offset = generation - 99
s.offset = 50000000000 - 99

print s.sum()
