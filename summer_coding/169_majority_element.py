class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        d = dict()
        
        t = list(set(nums))
        for i in t:
            d[i] = 0
            
        for i in nums:
            d[i] += 1
        
        for i in t:
            if d[i] > n:
                return i