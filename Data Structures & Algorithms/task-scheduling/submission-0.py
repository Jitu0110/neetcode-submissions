from collections import defaultdict, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #WE SHOULD PROCESS MAX FREQ FIRST
        maxHeap = []
        q = deque()
 
        freqDict = defaultdict(int)
        for task in tasks:
            freqDict[task] += 1
        interval = 0

        for task, freq in freqDict.items():
            heapq.heappush(maxHeap, [-freq,task]) # -2,X  -2,y


        while q or maxHeap:

            interval += 1

            if maxHeap:
                freq,task = heapq.heappop(maxHeap) 
                freq += 1 
                if freq < 0:
                    q.append([-freq,task,interval+n]) 
            
            if q and q[0][2] == interval: 
                freq, task, cooldown = q.popleft()
                heapq.heappush(maxHeap, [-freq,task])
        
        return interval
            
            
            



        