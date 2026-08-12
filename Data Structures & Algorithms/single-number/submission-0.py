class Solution:
    def singleNumber(self, nums: List[int]) -> int:
# a ^ a = 0 (a number XORed with itself cancels out)
# a ^ 0 = a (XOR with 0 keeps the number unchanged)
# XOR is commutative and associative, so order does not matter
        result = 0
        for num in nums:
            result = result ^ num
        
        return result

        