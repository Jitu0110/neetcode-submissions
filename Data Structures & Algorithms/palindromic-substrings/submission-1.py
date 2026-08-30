class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        #Time complexity brute force - O(n^2)
        #Explanation: n centers × up to n expansion steps = O(n²)

        for i in range(len(s)):
            l = r = i
            
            #Odd sized palindrome
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i+1
            
            #Even length palindrome
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

    # def countSubstrings(self, s: str) -> int:
        # res = 0

        # #Time complexity brute force - O(n^3)

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l, r = i, j
        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1
        #         res += (l >= r)

        # return res
