
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #nums = [1,2,1,0,4,2,6]
        #q = [1,2,3]
        #o = [2,]

        #Brute force - O(n * k) solution

        #Monotonically Decreasing Queue
        #Time - O(N) Space - O(N) (deque - O(K), output- O(N-k+1))
        output = []
        queue = deque() #holds indices
        left = right = 0

        while right < len(nums):

            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            #remove left val from window
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                output.append(nums[queue[0]])
                left += 1
            
            right += 1

        return output
            





        


        