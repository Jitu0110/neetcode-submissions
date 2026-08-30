class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:

    #     #bottom up
    #     #Space - O(N) Time - O(N)

    #     dp = [0] * (len(cost) + 1) #[0 0 0 0]

    #     #min cost to reach 0 index - 0
    #     #min cost to reach 1 index - 0


    #     for i in range(2,len(cost) + 1):
    #         dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]) # 0 0 1 2


    #     return dp[-1]


    # def minCostClimbingStairs(self, cost: List[int]) -> int:

    #     #Optimized bottom up
    #     #Space - O(1) Time - O(N)

    #     a = 0
    #     b = 0 
    #     c = 0

    #     #min cost to reach 0 index - 0
    #     #min cost to reach 1 index - 0


    #     for i in range(2,len(cost) + 1):
    #         c = min(b + cost[i-1], a + cost[i-2]) # 0 0 1 2
    #         a = b
    #         b = c


    #     return c


    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #Top down
        #Space - O(1) Time - O(N)



        #min cost to reach 0 index - 0
        #min cost to reach 1 index - 0

        cache = {}

        def dfs(n):
            if n == 1 or n == 0:
                return 0
            
            if n in cache:
                return cache[n]
            
            cache[n] = min(dfs(n-1)+cost[n-1], dfs(n-2) + cost[n-2])

            return cache[n]
        
        return dfs(len(cost))
            



        