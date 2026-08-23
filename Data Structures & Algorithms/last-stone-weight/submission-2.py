import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #maxheap
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, - stones[i])
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            result = x - y

            if result != 0:
                heapq.heappush(heap,-result)
        
        return 0 if len(heap) == 0 else -heap[0]
        