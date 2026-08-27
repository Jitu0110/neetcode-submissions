class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return res

#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         #Time - O(n * 2^n)
#         #Space -O(2^n)
        
# #THese are all duplicates!
# # [1, 1, 2]
# # [1, 2, 1]
# # [2, 1, 1]
#         res = set()
#         subset = []

#         def backtrack(i):
#             if i >= len(nums):
#                 res.add(tuple(subset))
#                 return

#             subset.append(nums[i])
#             backtrack(i + 1)
#             subset.pop()
#             backtrack(i + 1)

#         nums.sort()
#         backtrack(0)
#         return [list(s) for s in res]

        