class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) -1
        leftMax, rightMax = 0,0
        water = 0

        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right],rightMax)

            if leftMax <= rightMax:
                water += leftMax - height[left] 
                left += 1
            
            else:
                water += rightMax - height[right]
                right -= 1
        
        return water

        