import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countFreq = {}
        result = []

        for num in nums:
            countFreq[num] = countFreq.get(num,0)+1

        heap = []

        #NlogN
        for key in countFreq:
            heapq.heappush(heap,[-countFreq[key],key])
        
   
        #klogN
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


        