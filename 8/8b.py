class Numbers:
    def __init__(self, text):
        self.nums = map(int, text.split())
        
    def next(self):
        res = self.nums[0]
        self.nums = self.nums[1:]
        return res
    
    def next_list(self, count):
        res = self.nums[:count]
        self.nums = self.nums[count:]
        return res

def meta_sum(ns):
    res = 0

    children = ns.next()
    meta_count = ns.next()

    child_values = []
    for i in range(children):
        child_values.append(meta_sum(ns))

    meta_values = ns.next_list(meta_count)
    if children > 0:
        for v in meta_values:
            if v-1 < children:
                res += child_values[v-1]
    else:
        for v in meta_values:
            res += v
            
    return res

print meta_sum(Numbers(raw_input()))
