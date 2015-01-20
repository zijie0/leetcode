class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        zeros = 0
        while n >= 5:
            n = n / 5
            zeros += n
        return zeros

print Solution().trailingZeroes(14)

import math

print math.factorial(14)