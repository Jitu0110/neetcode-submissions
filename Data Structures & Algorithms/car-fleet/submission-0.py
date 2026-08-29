class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #speed = distance/time, time = distance/speed

        speedDict = {position[i] : speed[i] for i in range(len(position))}

        position.sort(reverse=True) #Descending

        stack = []

        for i in range(len(position)):
            timeTaken = (target-position[i])/speedDict[position[i]]
            if (stack and stack[-1] < timeTaken) or (len(stack) == 0):
                stack.append(timeTaken)
        
        return len(stack)


        