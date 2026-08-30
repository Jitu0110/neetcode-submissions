class Solution:
    def rob(self, nums: List[int]) -> int:
        #time - O(N) space - O(N)

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_range(left, right):

            a = 0
            b = 0

            for i in range(left, right + 1):
                c = max(b, a + nums[i])
                a = b
                b = c

            return b

        # Case 1: Don't rob first house
        case1 = rob_range(1, len(nums) - 1)

        # Case 2: Don't rob last house
        case2 = rob_range(0, len(nums) - 2)

        return max(case1, case2)