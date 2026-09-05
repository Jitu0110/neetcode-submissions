class Solution:

    #Brute force - Use +. / or something as delimiter. But this doesnt work

    #Best solution - Length Prefix encoding
    #[length] [delimiter] [exactly that many characters]
    #Delimiter can be anything
    # -> 5#Hello5#world


    #Time - O(N) , where N is total number of characters across all strings
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            strLen = len(s)
            res += str(strLen) + "#" + s
        
        return res


    # input -> 5#Hello5#world
    #Time - O(N) , where N is total number of characters across all strings
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the delimiter
            j = i
            while s[j] != "#":
                j += 1
            
            #Get length
            currLen = int(s[i:j])

            # Move past "#"
            j += 1

            res.append(s[j:j+currLen])

            i = j+currLen
        
        return res

            



        # while i+1 < lenStr and s[i+1] == "#": #This wont work, for more than 2 digit lengths(1st try failed
        # )
        #     currentLength = int(s[i])
        #     res.append(s[i+2:i+2+currentLength])
        #     i = i + 2 + currentLength
        
        # return res
        
