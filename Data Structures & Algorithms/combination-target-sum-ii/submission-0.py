class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #Time - O(N × 2^N)
    # Since there are 2^N combinations, and we copy each of them
        res = []
        
        #[1,2,2,4,5,6,9]
        candidates.sort()
        path = []

        def dfs(i,sum):
            if sum == target:
              res.append(path[:])
              return
            
            if sum > target:
              return
            
            for j in range(i,len(candidates)):
                #Skip duplicate paths. Example - [1,1,5,6] Target - 7. This will prevent [1,6] [1,6]
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                sum += candidates[j]
                path.append(candidates[j])

                dfs(j+1, sum)

                sum -= candidates[j]
                path.pop()




        dfs(0,0)
        return res
        