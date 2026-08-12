class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)

        # result = 0
        # carry = 0
        # position = 0

        # while a | b | carry:
        #     a_LSB = a & 1
        #     b_LSB = b & 1
        #     sum = a_LSB ^ b_LSB ^ carry
        #     carry = 1 if (a_LSB + b_LSB + carry) >= 2 else 0

        #     #update result. First shift sum to its right position and then OR with result
        #     result = result | (sum << position)

        #     a = a >> 1
        #     b = b >> 1
        #     position += 1

        # return result


#01
#001




               

        