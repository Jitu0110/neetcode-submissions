class Solution:
    def isHappy(self, n: int) -> bool:
        hSet = set()

        while True:
            x = 0
            while n:
                x = x + ((n%10)**2)
                n = n//10 #ALWAYS USE DOUBLE / IN PYTHON DIVISION!!!!!!!

            if x == 1:
                break

            if x in hSet:
                return False

            hSet.add(x)
            n = x
        
        return True
            
            

        