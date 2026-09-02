import collections
import heapq

class Solution:
    #Time - ElogV or ELogV (Each Pop/Push) - LogE. Number of times - E
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        

        for u, v, w in times:
            edges[u].append((v, w))

        distanceDict = {} #Finalized distances
        minHeap = [(0, k)] #Contains distance, Node 

        while minHeap:

            dist, v = heapq.heappop(minHeap)

            if v in distanceDict:
                continue

            distanceDict[v] = dist

            for v2, dist2 in edges[v]:
               if v2 not in distanceDict: 
                heapq.heappush(minHeap, (dist + dist2, v2))

        return max(distanceDict.values()) if len(distanceDict) == n else -1