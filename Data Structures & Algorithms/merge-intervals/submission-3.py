class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Time - O(Nlogn)

        if not intervals:
           return []

        #Nlogn 
        intervals.sort(key=lambda x:x[0])
        
        curr = intervals[0]
        res = []
        
        #n
        for i in range(1,len(intervals)):
            if curr[1] >= intervals[i][0] and curr[0] <= intervals[i][1]:
                curr[0] = min(curr[0],intervals[i][0])
                curr[1] = max(curr[1],intervals[i][1])
            else:
                res.append(curr)
                curr = intervals[i]
        
        res.append(curr)

        return res








