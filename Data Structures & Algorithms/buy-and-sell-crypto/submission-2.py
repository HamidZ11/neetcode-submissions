class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices is an array where prices[i] is the price
        #find the max profit you can make, you can buy at any day and sell any day in future

        #for each day in prices you need to find the max price you can sell at 

        max_profit = 0 
        current_profit = 0
        cheapest_price = prices[0]

        for i in prices: 
            if i < cheapest_price:
                cheapest_price = i
            else:
                current_profit = i - cheapest_price
                if current_profit > max_profit:
                    max_profit = current_profit
        
        return max_profit

