class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 
        max_profit = 0
        current_profit = 0

        for right in range(len(prices)):
            current_profit = prices[right] - prices[left] 

            while prices[right] < prices[left]:
                left+= 1
            
            max_profit = max(max_profit, current_profit)
        
        return max_profit


        




