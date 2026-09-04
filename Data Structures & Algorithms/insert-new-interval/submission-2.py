class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #time - O(N)
        #Linear Search
        #Just need to update the 'newInterval' itself if there is an overlap, with min and max

        n = len(intervals)
        i = 0
        res = []

        #intervals = [[1,3], [5,7], [6,9], [10,12]]
        #newInterval = [4,6]

        #End time of existing interval is before starting of new interval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2 intervals overlap when
        # existing_start <= new_end
        # AND
        # existing_end >= new_start
        while i < n and (intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
        
# Greedy solution!      
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []

#         for i in range(len(intervals)):
#             if newInterval[1] < intervals[i][0]:
#                 res.append(newInterval)
#                 return res + intervals[i:]
#             elif newInterval[0] > intervals[i][1]:
#                 res.append(intervals[i])
#             else:
#                 newInterval = [
#                     min(newInterval[0], intervals[i][0]),
#                     max(newInterval[1], intervals[i][1]),
#                 ]
#         res.append(newInterval)
#         return res


        