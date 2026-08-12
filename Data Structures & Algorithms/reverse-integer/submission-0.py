class Solution:
    def reverse(self, x: int) -> int:
        #Time - O(D) where D is digits
        isPositive = True
        if(x<0):
            isPositive = False

        x = abs(x)

        result = 0
        while x:
            rem = x % 10 #4 , 3, 2, 1
            x = x // 10 #123, 12, 1, 0
            result = (result * 10) + rem #4,43,432,4321
        
        #Handle 32-bit integer overflow
        #Valid range- -2,147,483,648 to 2,147,483,647
        if result > 2**31 - 1:
            return 0

        return result if isPositive else -result

        

            
        