"""
Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
Follow up:
If this function is called many times, how would you optimize it?
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        l = list(bin(n))[2:]
        l.reverse()
        n = len(l)
        print(n)
        if n < 32:
            for _ in range(32-n):
                l.append('0')
        print(l)
        return int(''.join(l), 2)

s = Solution()
print(s.reverseBits(1))