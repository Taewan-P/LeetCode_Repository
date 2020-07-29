class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = dict()
        for n in nums:
            if n in occ:
                occ[n] += 1
            else:
                occ[n] = 1
  
        top_items = sorted(occ.items(), key=lambda x:x[1], reverse=True)[:k]
       
        return [n[0] for n in top_items]