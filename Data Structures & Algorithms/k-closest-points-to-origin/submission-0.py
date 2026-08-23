class Solution:
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     minHeap = []
    #     #Total time - O(N + k log N)

    #     #Time - O(N)
    #     for x, y in points:
    #         dist = (x ** 2) + (y ** 2)
    #         minHeap.append([dist, x, y])

    #     #Time - O(N)
    #     heapq.heapify(minHeap)
    #     res = []

    #     #Time - k log(N)
    #     while k > 0:
    #         dist, x, y = heapq.heappop(minHeap)
    #         res.append([x, y])
    #         k -= 1

    #     return res


        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            maxHeap = []
            #Total time - O(Nlogk)

            #Time - O(N)
            for x, y in points:
                dist = (x ** 2) + (y ** 2)
                heapq.heappush(maxHeap,[-dist, x, y])

                if len(maxHeap) > k:
                    heapq.heappop(maxHeap) #logk
                

            res = []

            #Time - k log(k)
            while maxHeap:
                dist, x, y = heapq.heappop(maxHeap)
                res.append([x, y])

            return res