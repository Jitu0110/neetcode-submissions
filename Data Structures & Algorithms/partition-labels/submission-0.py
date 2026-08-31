class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Time - O(N)
        #Logic: Every time you encounter a character whose last occurrence is farther away, you extend end.

        lastIndex = {}
        result = []

        for i in range(len(s)):
            lastIndex[s[i]] = i  #{x:3, y : 4, z:7, b:9, i: 10 , s: 11 , l: 12 }
        

        end = 0
        partitionLength = 0

        for i in range(len(s)):

            partitionLength += 1

            end = max(end,lastIndex[s[i]]) 

            if i == end:
                #partition reached
                result.append(partitionLength)
                partitionLength = 0
        
        return result
            



            


        
        

        