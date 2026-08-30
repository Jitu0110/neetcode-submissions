class Solution:
    # def climbStairs(self, n: int) -> int:

    #     #Distinct ways I can take 1 stair - 1
    #     #Distinct ways I can reach 2 Stairs - 2
    #     #Distinct ways I can reach 3 Stairs - From 2nd stair, take 1 step or from 1st stair, taking 2 steps
        
    #     #Bottom up
    #     # Time - O(n) Space - O(1)
    #     a = 1
    #     b = 1
    #     c = 0
        
    #     for i in range(2,n+1):
    #         c = a + b
    #         a = b
    #         b = c
        
    #     return c
        def climbStairs(self, n: int) -> int:

        #Distinct ways I can take 1 stair - 1
        #Distinct ways I can reach 2 Stairs - 2
        #Distinct ways I can reach 3 Stairs - From 2nd stair, take 1 step or from 1st stair, taking 2 steps
        
        #Top down
        # Time - O(n) Space - O(n)

            cache = {}

            def dfs(n):

                if n == 1 or n == 0:
                    return 1
                
                if n in cache:
                    return cache[n]

                cache[n] = dfs(n-1) + dfs(n-2)

                return cache[n]
            
            return dfs(n)

                


        



        