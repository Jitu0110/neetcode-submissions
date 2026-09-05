class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Time - O(log(min(m, n)))
        #Intuition:
        #A = [ elements on LEFT | elements on RIGHT ]
        #B = [ elements on LEFT | elements on RIGHT ]
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        #At this stage, A is the shorter list  

        l, r = 0, len(A) - 1

        #Binary search on A
        while True:
            #number of elements in A left = i + 1
            #number of elements in B left = j + 1
            # half = i + 1 + j + 1
            # j = half - i -2
            i = (l + r) // 2 #i is half on A
            j = half - i - 2 #j is half on B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1