# valid condition -> k >= (right - left + 1) - max frq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Time - O(N) space - O(1)
        # s = "XYYX", k = 2

        left = 0 
        maxCount = 0
        myDict = {}
        result = 0
    

        for right in range(len(s)):

            #Update count in dictionary
            myDict[s[right]] = myDict.get(s[right],0) + 1
 
            #Update maxCount val
            maxCount = max(maxCount, myDict[s[right]])

            #check for invalid condition and move left
            # If the number of replacements needed is greater than k, shrink the window.
            while(((right - left + 1) - maxCount) > k):
                myDict[s[left]] = myDict.get(s[left],0) - 1
                left += 1 

            result  = max(result, right - left + 1)
        return result 







        