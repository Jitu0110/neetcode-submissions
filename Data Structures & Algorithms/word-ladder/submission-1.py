class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        #Space - We create m patterns per word worst case, total patterns N*M. 
        #Each pattern is of size 'm'. so total - o(N*m^2)
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        #Time - n*m*m = o(N*m^2)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:] #O(m)
                nei[pattern].append(word)
        
        #BFS
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        # For every word we visit, we go through each character and create pattern
        # O(N*M*M) = o(N*m^2)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        
        return 0





        

        