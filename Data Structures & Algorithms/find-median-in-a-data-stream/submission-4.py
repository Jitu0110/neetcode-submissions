class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:

        if self.maxHeap and num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)

        elif self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)

        else:
            heapq.heappush(self.maxHeap, -num)

        # Always rebalance AFTER insertion!!!!
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(
                self.minHeap,
                -heapq.heappop(self.maxHeap)
            )

        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(
                self.maxHeap,
                -heapq.heappop(self.minHeap)
            )


    def findMedian(self) -> float:
        if len(self.maxHeap ) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]
            
   



