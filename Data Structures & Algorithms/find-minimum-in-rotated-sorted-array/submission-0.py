class Solution:
    def findMin(self, nums: List[int]) -> int:
        #time - O(log(n))

        #logic: Using binary search, either l and mid will be in one sorted half OR r and mid will be one sorted half
        # Questions for if else: Could mid still be the answer? Yes - keep it, else ignore it


        left, right = 0, len(nums) - 1

        while(left < right):

            mid = left + (right-left)//2

            if nums[mid] > nums[right]:
                #solution in right half
                left = mid + 1
            else:
                right = mid

        
        return nums[left]

