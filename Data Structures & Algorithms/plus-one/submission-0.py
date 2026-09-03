class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        carry = 0
        i = len(digits)-1
        carry = 1
        while i >= 0:
            total = carry + digits[i]

            carry = total // 10
            total = total % 10

            res.append(total)
            i -= 1 
        
        if carry !=0:
            res.append(carry)
        
        res.reverse()

        return res
        
