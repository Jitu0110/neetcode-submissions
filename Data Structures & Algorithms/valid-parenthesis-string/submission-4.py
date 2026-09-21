class Solution:
    # def checkValidString(self, s: str) -> bool:
    #     #This is Brute force - Time Complexity of 3^n, Space is O(N) recursion
        
    #     def dfs(i,openN,closedN):

    #         if closedN > openN:
    #             return False
            
    #         if i == len(s):
    #             if openN == closedN:
    #                 return True
    #             else: 
    #                 return False
            
            
    #         if s[i] == "(" :
    #             return dfs(i+1, openN + 1, closedN)
    #         elif s[i] == ")":
    #             return dfs(i+1, openN, closedN + 1)
    #         else : # *
    #             return (dfs(i+1, openN + 1, closedN) or# taking ) option
    #             dfs(i+1, openN, closedN + 1)or # taking ( option
    #             dfs(i+1, openN, closedN)) # Taking "" option



    #     return dfs(0,0,0)

    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0 #Number of open '(' , minimum and maximum

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if leftMax < 0: #Even under the most optimistic interpretation, we have too many ).
                return False

            if leftMin < 0: #We know that some interpretations have gone negative, but as long as at least one valid interpretation exists, the minimum possible number of open parentheses is effectively 0.
                leftMin = 0

        
        return leftMin == 0 #why? 
            
            


        
        