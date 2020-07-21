class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        occ = dict()
        for w in words:
            if w in occ:
                occ[w] += 1
            else:
                occ[w] = 1
                
        items = list(occ.items())  
        top_items = sorted(occ.items(), key=lambda x:x[1], reverse=True)[:k]
       
        return [w[0] for w in top_items]