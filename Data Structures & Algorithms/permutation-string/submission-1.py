class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #Time - O(N) Space - O(1)

        #Invalid case

        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False


        dict_s1, dict_s2 = {}, {}

        for char in s1:
            dict_s1[char] = dict_s1.get(char,0) + 1

            # dict_s1 is {"a": 1, "b" : 1, "c": 1}
        

        left = 0
        
        for right in range(s2_length):
            
            # add right element to window
            dict_s2[s2[right]] = dict_s2.get(s2[right],0) + 1

            # shrink window if its greater than length of s1
            if right - left + 1 > s1_length:
                left_char = s2[left]

                dict_s2[left_char] -= 1

                if dict_s2[left_char] == 0:
                    del dict_s2[left_char]

                left += 1
            
            if dict_s1 == dict_s2:
                return True

        return False

