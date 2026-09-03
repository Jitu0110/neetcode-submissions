
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Time: O(m * n)
        # Space: O(n)

        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]

    # def uniquePaths(self, m: int, n: int) -> int:

    #     #Time-O(M*N)
    #     #Space - O(M*N)

    #     if m==1 and n==1:
    #         return 1

    #     dp = [[0] * n for _ in range(m)]


    #     dp[0][0] = 0

    #     for i in range(1,n):
    #         dp[0][i] = 1
        
    #     for j in range(1,m):
    #         dp[j][0] = 1

    #     for i in range(1,m):
    #         for j in range(1,n):
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
    #     return dp[m-1][n-1]

        