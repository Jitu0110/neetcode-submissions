class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Time - O(n)

        result = 0

        #XOR all numbers that should be in range - [0 ^ 0 ^ 1 ^ 2 ^ 3]
        for i in range(len(nums)+1):
            result = result ^ i


        #Then XOR the numbers that are present. Since a^a = 0, they will cancel out leaving just the missing number left
        for i in range(len(nums)):
            result = result ^ nums[i]
        
        return result
        


        #Time - O(n^2)
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        # return 0