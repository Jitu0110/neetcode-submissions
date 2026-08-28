class Solution:
    #Time - O(N × N!)
    # Trick here is to send the picked information , using pick boolean List
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                #Use the number
                perm.append(nums[i])
                pick[i] = True

                self.backtrack(perm, nums, pick)

                #Remove the number
                perm.pop()
                pick[i] = False

        