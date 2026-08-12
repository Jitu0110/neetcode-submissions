class Solution:
    def countBits(self, n: int) -> List[int]:
        #Time - O(N) DP

        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

        result = [0]* (n+1)


# O(nlogn) solution
# for i in range(n+1):
#     count = 0
#     num = i
#     while num:
#         count += num & 1
#         num >>= 1
#     result[i] = count

# return result


#3) Inbuilt way - O(nlogn)
# return [bin(i).count('1') for i in range(n + 1)]

        