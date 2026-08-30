class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Kadane algo adapted for products = curMax and curMin, 
        # curMax - max product ending at this index
        # curMin - min product ending at this index
        # curMin is important bcause if current number is -ve, multiplying with curMin might produce new max
        res = float("-inf")

        curMin, curMax = 1,1

        for num in nums:
            temp = curMax
            curMax = max(num * curMax, num * curMin, num) # We need num in end incase of 0 coming previously
            curMin = min(num * temp, num * curMin, num )
            res = max(res, curMax)
        return res
    # def maxProduct(self, nums: List[int]) -> int:
    #     #time brute force - o(n^2)
    #     res = nums[0]

    #     for i in range(len(nums)):
    #         cur = nums[i]
    #         res = max(res, cur)
    #         for j in range(i + 1, len(nums)):
    #             cur *= nums[j]
    #             res = max(res, cur)

    #     return res