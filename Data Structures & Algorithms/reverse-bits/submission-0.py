class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            num = (result << 1)
            result = num | (n & 1)
            n >>= 1

        return result

# This is O(32) = O(1) time and O(1) space.

# The key idea is: take the rightmost bit of n, put it into result, then shift n right and repeat 32 times.