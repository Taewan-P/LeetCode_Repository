class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        
        for i in range(len(prices)):
            tmp = prices[i+1:]
            if tmp:
                profit.append(max(tmp) - prices[i])
        
        if not profit:
            return 0
        else:
            result = max(profit)
            return result if result > 0 else 0