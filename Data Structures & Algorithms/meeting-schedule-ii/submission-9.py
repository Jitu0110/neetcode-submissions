"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # The min-heap tracks the end times of currently occupied meeting rooms. The smallest end time (minHeap[0]) tells us which room becomes available first.

        intervals.sort(key=lambda x: x.start) #n log n

        minHeap = [] #Stores meeting end times

        for i in range(len(intervals)):
           if minHeap and intervals[i].start >= minHeap[0]: #can reuse same room
               heapq.heappop(minHeap) #nlogn
           heapq.heappush(minHeap, intervals[i].end)
        
        return len(minHeap)



 



        