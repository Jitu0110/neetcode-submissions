class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Time - O(N) Space - O(N)
        myDict = {}
        
        for i,num in enumerate(nums):
            if target - num in myDict:
                complementIndex = myDict.get(target-num)
                return [complementIndex,i] 
                #a if cond else b (equal to ternary in Java)
            else:
                myDict[num] = i
        
# 1) 0 is false in python, this wont work - if myDict.get(target-num):
# 2) python doesnt have a ternary operator ? -> a if condition else b
        