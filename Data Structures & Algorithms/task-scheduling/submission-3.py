from collections import defaultdict, deque
import heapq
class Solution:
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     #Time - O(NlogN) and space - O(N)

    #     #WE SHOULD PROCESS MAX FREQ FIRST
    #     maxHeap = [] # #O(N) Space
    #     q = deque() #O(N) Space
 
    #     freqDict = defaultdict(int) #O(N) Space
    #     for task in tasks:
    #         freqDict[task] += 1
    #     interval = 0

    #     #Time - Nlogn where N is task, assuming there were N unique tasks(Worst case)
    #     for task, freq in freqDict.items():
    #         heapq.heappush(maxHeap, [-freq,task]) # -2,X  -2,y


    #     while q or maxHeap:

    #         interval += 1

    #         if maxHeap:
    #             freq,task = heapq.heappop(maxHeap) 
    #             freq += 1 
    #             if freq < 0:
    #                 q.append([-freq,task,interval+n]) 
            
    #         if q and q[0][2] == interval: 
    #             freq, task, cooldown = q.popleft()
    #             heapq.heappush(maxHeap, [-freq,task])
        
    #     return interval

        def leastInterval(self, tasks: List[str], n: int) -> int:

            freq = [0] * 26

            for task in tasks:
                freq[ord(task) - ord('A')] += 1

            maxFreq = max(freq)

            maxFreqCount = freq.count(maxFreq)

            intervals = (maxFreq - 1) * (n + 1) + maxFreqCount

            return max(len(tasks), intervals)
            
            
            



        