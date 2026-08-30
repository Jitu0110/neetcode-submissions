class Solution:

    def rob(self, nums: List[int]) -> int:


        #Bottom Up optimized
        #Time - O(N) Space - O(1)

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        a = nums[0]
        b = max(nums[0], nums[1])


        for i in range(2,len(nums)):
            c = max(b, a + nums[i]) 
            a = b
            b = c
        
        return b


    # def rob(self, nums: List[int]) -> int:


    #     #Bottom Up
    #     #Time - O(N) Space - O(N)

    #     if nums and len(nums) == 1:
    #         return nums[0]

    #     #dp[i] stores max amount of money that can be robbed till ith house, going left to right
    #     #I.e dp[i] stoes max(robbing current house + robbing 2 house ago max, robbing 1 house ago)

    #     dp = [0] * len(nums) #[0 0 0 0]

    #     dp[0] = nums[0]
    #     dp[1] = max(nums[0], nums[1])



    #     for i in range(2,len(nums)):
    #         dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 
        
    #     return dp[-1]


        