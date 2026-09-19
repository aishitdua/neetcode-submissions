class MinStack:
    def __init__(self):
        self.l = []
        self.min_vals = []
        return None
        

    def push(self, val):
        self.l.append(val)
        new_min = val if not self.min_vals else min(val,self.min_vals[-1])
        self.min_vals.append(new_min)
    

    def pop(self):
        self.l.pop()
        self.min_vals.pop()     

    def top(self) -> int:
        return self.l[-1]

    def getMin(self):
        return self.min_vals[-1]
