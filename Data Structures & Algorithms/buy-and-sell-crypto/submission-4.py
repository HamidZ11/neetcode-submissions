class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 
        max_profit = 0
        current_profit = 0

        for right in range(len(prices)):
            current_profit = prices[right] - prices[left] 

            if prices[right] < prices[left]:
                left = right
            
            max_profit = max(max_profit, current_profit)
        
        return max_profit


        




