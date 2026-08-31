"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)

        minHeap = [] #Stores meeting end times

        for i in range(len(intervals)):
           if minHeap and intervals[i].start >= minHeap[0]: #can reuse same room
               heapq.heappop(minHeap)
           heapq.heappush(minHeap, intervals[i].end)
        
        return len(minHeap)



 



        