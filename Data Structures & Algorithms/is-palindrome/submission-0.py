class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Normalize s
        s_list = [ch.lower() for ch in s if ch.isalnum()]

        l,r = 0, len(s_list)-1

        while l < r:
            if s_list[l] != s_list[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        