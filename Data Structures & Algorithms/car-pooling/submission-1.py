import heapq

class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        #Nlogn
        trips.sort(key=lambda t: t[1])

        minHeap = [] # pair of end, numPassengers
        currPass = 0 
        
        # O(N)
        for numPass, start, end in trips:

            # Worst case - N log n
            while minHeap and minHeap[0][0] <= start:
                currPass -= heapq.heappop(minHeap)[1]

            currPass += numPass

            if currPass > capacity:
                return False

             # Worst case - N log n
            heapq.heappush(minHeap, [end,numPass])
        
        return True





    # Time - O(n**2)
    # def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

    #     trips.sort(key=lambda x:x[1])

    #     for i in range(len(trips)):
    #         curPass = trips[i][0]
            
    #         #Are the passengers from the previous trip still in the car when this trip starts?
    #         # O (N^2)
    #         for j in range(i):
    #             if trips[j][2] > trips[i][1]:
    #                 curPass += trips[j][0]

    #         if curPass > capacity:
    #             return False

        
    #     return True
        