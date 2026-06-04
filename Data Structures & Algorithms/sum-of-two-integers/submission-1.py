class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # para simular 32 bits
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        # tratamento de número negativo
        return a if a <= max_int else ~(a ^ mask)