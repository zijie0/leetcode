class Solution:
    # @return an integer
    max_int = 2147483647
    def reverse(self, x):
        result = 0
        neg = False
        if x < 0:
            x = -x
            neg = True
        while x > 0:
            result = result * 10 + x % 10
            x = x / 10
        if result > self.max_int:
            return 0
        return result if not neg else -result

print Solution().reverse(1534236469)