class Solution:
    #Time - O(N × N!)
    # Trick here is to send the picked information , using pick boolean List
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm: List[int], nums: List[int], pick: List[bool]):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in range(len(nums)):
                if not pick[i]:
                    #Use the number
                    perm.append(nums[i])
                    pick[i] = True

                    backtrack(perm, nums, pick)

                    #Remove the number
                    perm.pop()
                    pick[i] = False

        backtrack([], nums, [False] * len(nums))

        return res



        