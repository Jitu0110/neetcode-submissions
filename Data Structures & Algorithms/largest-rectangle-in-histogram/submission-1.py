class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #monotonic increasing stack
        #As long as the next bar is taller or equal, we keep pushing indices.

#TIme complexity - O(N) Space - O(N)
# pushed once
# popped at most once
        maxArea = float("-inf")

        stack = []

        for i in range(len(heights)):
           lastPoppedIndex = -1
           while stack and stack[-1][0] > heights[i]: #We found a lower height, process and calculate area        
                 height, index = stack.pop()
                 maxArea = max(maxArea, height * (i-index))
                 lastPoppedIndex = index
              
           stack.append((heights[i],i)) if lastPoppedIndex == -1 else stack.append((heights[i],lastPoppedIndex))
        
        while stack:
            height, index = stack.pop()
            maxArea = max(maxArea, height * (len(heights)-index))
            print(height * (len(heights)-index))
        
        return maxArea


        