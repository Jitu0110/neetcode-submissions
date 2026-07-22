class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time - O(N) Space - O(Min(m,n)), where n is length of string, m is unique characters
        hashSet = set()
        left = 0

        longestSubstring = 0

        for right in range(len(s)):
            # s = "zxyzxyz"
            # right goes from 0 to 6
            while(s[right] in hashSet):
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right])
            longestSubstring = max(longestSubstring, right - left + 1)

        return longestSubstring
            

                
            
           
            



