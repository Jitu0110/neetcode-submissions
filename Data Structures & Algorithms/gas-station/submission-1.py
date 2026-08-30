class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): #If solution doesn't exist
            return -1 

        if len(gas) != len(cost):
            return -1

        gasBalance = 0
        result = 0
        for i in range(len(gas)): #i goes from 0 to 3
            gasBalance += gas[i] - cost[i] #-1 result 1, 

            if gasBalance < 0:
                gasBalance = 0
                result = i + 1
        
        return result






        
        