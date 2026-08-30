class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * (len(cost) + 1) #[0 0 0 0]

        #min cost to reach 0 index - 0
        #min cost to reach 1 index - 0


        for i in range(2,len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]) # 0 0 1 2


        return dp[-1]



        