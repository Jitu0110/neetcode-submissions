class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Time - O(N)

        triplet = [0, 0, 0]

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            triplet = [max(triplet[0],t[0]), max(triplet[1],t[1]), max(triplet[2],t[2])]
        
        return triplet == target



        