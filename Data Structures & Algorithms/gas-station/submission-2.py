class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): #If solution doesn't exist
            return -1 

        if len(gas) != len(cost):
            return -1

        gasBalance = 0
        result = 0
        for i in range(len(gas)): 
            gasBalance += gas[i] - cost[i] 

            if gasBalance < 0:
                gasBalance = 0
                result = i + 1
        
        return result






        
        