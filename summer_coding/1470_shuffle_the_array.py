class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[:n]
        b = nums[n:]
        
        result = []
        
        for i in range(n):
            result.append(a[i])
            result.append(b[i])
            
        return result