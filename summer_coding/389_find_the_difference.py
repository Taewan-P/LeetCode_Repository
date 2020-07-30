class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = dict()
        d2 = dict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
                
        return [t for t in d2.items() if not t in d.items()][0][0]