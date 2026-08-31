from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Time Complexity - O(N) As we process each card at most once
        #Space Complexity - O(N) as we use the freqDict
        # Learning - dont use defaultdict, it can create entry into dict by mistake 

        if not hand:
            return False

        if len(hand) % groupSize != 0:
            return False

        freqDict = {}

        # Build frequency dictionary
        for num in hand:
            freqDict[num] = freqDict.get(num, 0) + 1

        # Try to build groups
        for num in hand:

            # This card was already used
            if freqDict.get(num, 0) == 0:
                continue

            while freqDict.get(num-1, 0) > 0: #Go to start of group!! Important
                num = num - 1

            temp = num
            targetGroupSize = groupSize

            while targetGroupSize > 0:

                # Required card doesn't exist / was already used
                if freqDict.get(temp, 0) == 0:
                    return False

                freqDict[temp] -= 1

                temp += 1
                targetGroupSize -= 1

        return True