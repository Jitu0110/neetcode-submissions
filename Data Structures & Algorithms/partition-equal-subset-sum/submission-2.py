class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0: #Cant partition for odd sum
            return False

        target = sum(nums)//2

        def dfs_backtrack(i, sum):

            if sum > target:
                return
            
            if sum == target:
                return True
            
            for j in range(i,len(nums)):
               if dfs_backtrack(j+1, sum + nums[i]):
                   return True
            return False

        return dfs_backtrack(0,0)
                
            


        