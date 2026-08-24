class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict = defaultdict(list)

        for str in strs:
            freq = [0] * 26

            for char in str:
                freq[ord(char)- ord('a')] += 1

            anagramDict[tuple(freq)].append(str)
        
        return list(anagramDict.values())
        

            
            



        