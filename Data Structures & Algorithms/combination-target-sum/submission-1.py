class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #Time complexity : O(N^(T/M))
# Where:

# N = number of candidates in nums
# T = target
# M = smallest number in nums
        res = []
     
        path = []

        def dfs(i, sum):
            if sum == target:
                res.append(path[:])
                return
            
            if sum > target:
                return
            
            for j in range(i, len(nums)):
                #Take the number in path
                sum += nums[j]
                path.append(nums[j])

                dfs(j,sum)

                #Remove the number in path
                sum -= nums[j]
                path.pop()

        
        dfs(0,0)

        return res





            



            

        