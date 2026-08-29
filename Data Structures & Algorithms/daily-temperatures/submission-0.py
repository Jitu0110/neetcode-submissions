class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #Monotonic decreasing stack 
        # When we find larger number than top, we pop
        #Time - O(N) Space - O(N)
        stack = []
        result = [0] * len(temperatures)

        for i in range(0,len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                temp,index = stack.pop()
                result[index] = i - index
            
            stack.append([temperatures[i],i])
        
        return result

        