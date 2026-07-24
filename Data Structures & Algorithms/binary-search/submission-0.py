class Solution:
    def search(self, nums: List[int], target: int) -> int:


        left,right = 0, len(nums)-1

        while left <= right:

            #mid = (left + right)//2 (1)

            # now right = left + (right - left), subsititute in 1

            # mid = (2left + (right-left))/2

            mid = left + (right-left)//2 #avoids integer overflow

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else :
                left = mid + 1
        
        return -1

        