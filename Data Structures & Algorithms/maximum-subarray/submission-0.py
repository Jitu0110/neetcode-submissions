class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        res = float("-inf")

        for num in nums:
            sum += num

            res = max(res,sum)

            if sum < 0:
                sum = 0
            
        return res
      




        