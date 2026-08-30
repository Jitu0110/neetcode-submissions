class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

# Let:
# n = len(s)
# m = len(wordDict)
# k = average/max length of a word
# Time Complexity: O(n × m × k)

        dp = [False] * (len(s)+1)
        dp[len(s)] = True #Base case 

        for i in range(len(s)-1,-1,-1):

            for w in wordDict:

                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:

                      dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break
        
        return dp[0]