class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        
        prod = 1

        for i in range(1,len(nums)):
            prod = prod * nums[i-1]
            result[i] = prod
        #[1 1 2 8]

        rightProd = 1

        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i] * rightProd
            rightProd = rightProd * nums[i]
        
        return result
        

        

