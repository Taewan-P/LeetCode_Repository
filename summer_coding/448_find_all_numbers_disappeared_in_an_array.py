class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = dict()
        
        for i in range(1,len(nums)+1):
            index[i] = 0
        
        for i in nums:
            index[i] += 1

        return list(filter(lambda x: index[x] == 0, range(1,len(nums)+1)))