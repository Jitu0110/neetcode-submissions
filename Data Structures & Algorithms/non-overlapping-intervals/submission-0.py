class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #Trick: Sort by end time!
        #We want to keep intervals that finish as early as possible.
        #Because an interval that ends earlier leaves more room for future intervals.

        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]


        return res

        #Example: intervals = [[1,2], [1,3], [2,3], [3,4]]