class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Time - O(N) Space - O(1)

        profit = float('-inf')  
        leastSoFar = float('inf') 

        for price in prices:
            if price < leastSoFar:
                leastSoFar = price
            
            profit = max(price - leastSoFar, profit)
        
        return profit

             

        