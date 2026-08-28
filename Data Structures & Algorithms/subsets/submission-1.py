class Solution:

    #Time complexity - (2^N * N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            res.append(subset[:])
            
            for j in range(i,len(nums)):
                subset.append(nums[j])

                dfs(j+1)

                subset.pop()


        dfs(0)
        return res
        