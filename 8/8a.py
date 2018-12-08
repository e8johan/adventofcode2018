class Numbers:
    def __init__(self, text):
        self.nums = map(int, text.split())
        
    def next(self):
        res = self.nums[0]
        self.nums = self.nums[1:]
        return res

def meta_sum(ns):
    res = 0

    children = ns.next()
    meta_count = ns.next()
    
    while children > 0:
        res += meta_sum(ns)
        children -= 1
    
    while meta_count > 0:
        res += ns.next()
        meta_count -= 1
        
    return res

print meta_sum(Numbers(raw_input()))
