import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Time - nlogk
        countFreq = {}
        result = []

        for num in nums:
            countFreq[num] = countFreq.get(num,0)+1

        heap = []

        #min heap - nlogk
        for key in countFreq:
            heapq.heappush(heap,[countFreq[key],key])

            if len(heap) > k:
                heapq.heappop(heap)

        #klog k
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result



        #Time - Nlogn
        # countFreq = {}
        # result = []

        # for num in nums:
        #     countFreq[num] = countFreq.get(num,0)+1

        # heap = []

        # #NlogN
        # for key in countFreq:
        #     heapq.heappush(heap,[-countFreq[key],key])
        
   
        # #klogN
        # for _ in range(k):
        #     result.append(heapq.heappop(heap)[1])

        # return result


        