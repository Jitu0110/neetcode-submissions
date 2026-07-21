class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # mySet = set()

        # for n in nums:
        #     if n in mySet:
        #         return True
        #     else:
        #         mySet.add(n)
        # return False

        