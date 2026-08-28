class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []

        def backtrack(i):
            res.append(subset[:])

            for j in range(i, len(nums)):

                # Skip duplicate choices at the same level
                if j > i and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])

                backtrack(j + 1)

                subset.pop()


        
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

        