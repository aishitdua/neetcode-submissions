class Solution:
    def isValid(self, s: str) -> bool:
        o = []
        c = []
        d = {"[":"]","{":"}","(":")"}
        for i in s:
            if i in ("[","{","("):
                o.append(i)
            else:

                if len(o)==0 or d[o[-1]] != i:
                    return False
                else:
                    o.pop()
        if len(o):
            return False
        return True
    
