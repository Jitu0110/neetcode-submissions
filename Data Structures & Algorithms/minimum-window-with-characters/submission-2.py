class Solution:
    def minWindow(self, s: str, t: str) -> str:

# IF: 

# S = len(s)
# T = len(t)
# K = number of unique characters in t

# Your solution has:

# Time: O(S × K)

        if len(t) > len(s):
            return ""

        dict_t, dict_s = defaultdict(int), defaultdict(int)

        resStartIndex, minLength= 0,float("inf")

        for char in t:
            dict_t[char] += 1
        
        left=0

        for right in range(len(s)):
            dict_s[s[right]] += 1

            while(self.isSubstring(dict_t,dict_s)):
                if right-left+1 < minLength:
                      minLength = right-left+1
                      resStartIndex = left
                charLeft = s[left]
                dict_s[charLeft] -= 1
                left += 1
        return s[resStartIndex:resStartIndex+minLength] if minLength != float("inf") else ""


    
    # Time - O(1)?
    def isSubstring(self, dict_t: dict, dict_s:dict) -> bool:
        for key in dict_t:
            if dict_s[key] < dict_t[key]: #It should be equal to or greater for valid substring
                return False
        return True




        