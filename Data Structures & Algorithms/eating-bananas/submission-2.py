class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if not piles or len(piles) == 0:  
            return 0

        right, left = max(piles), 1

        # 1 2 3 4, right = 4 left = 1 mid = 2 ,  right = 2 left = 1 

        while(left < right):

            mid = left + (right - left)//2

            timeTaken = 0
            for i in range(len(piles)):
                timeTaken += piles[i]//mid

                if piles[i] % mid != 0:
                    timeTaken += 1
            
            if timeTaken > h:
                left = mid + 1 
            
            else: 
                right = mid 
        
        return right

            










        


        