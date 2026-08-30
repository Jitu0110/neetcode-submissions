class Solution:
    def climbStairs(self, n: int) -> int:

        #Distinct ways I can take 1 stair - 1
        #Distinct ways I can reach 2 Stairs - 2
        #Distinct ways I can reach 3 Stairs - From 2nd stair, take 1 step or from 1st stair, taking 2 steps
        
        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]



        