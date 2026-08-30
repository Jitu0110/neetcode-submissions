class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxLen = 0
        start,end = 0,0

        #Time complexity brute force - O(n^2)
        #Explanation: n centers × up to n expansion steps = O(n²)

        for i in range(len(s)):
            l = r = i
            
            #Odd sized palindrome
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    start = l
                    end = r
                l -= 1
                r += 1
            
            l = i
            r = i+1
            
            #Even length palindrome
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    start = l
                    end = r
                l -= 1
                r += 1

        return s[start:end+1]
        