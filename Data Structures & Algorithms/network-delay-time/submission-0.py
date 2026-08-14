import collections
import heapq

class Solution:
    #Time - ElogV or ELogV (Each Pop/Push) - LogE. Number of times - E
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:

            dist, v = heapq.heappop(minHeap)

            if v in visited:
                continue

            visited.add(v)
            t = dist

            for v2, dist2 in edges[v]:
               if v2 not in visited: 
                heapq.heappush(minHeap, (dist + dist2, v2))

        return t if len(visited) == n else -1