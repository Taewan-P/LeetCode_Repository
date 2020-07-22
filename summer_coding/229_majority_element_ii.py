class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occ = dict()
        length = len(nums)/3
        result = []
        
        for i in nums:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1       
        
        num_dic = list(occ.items())
        
        for i,j in num_dic:
            if j > length:
                result.append(i)
                
        return result