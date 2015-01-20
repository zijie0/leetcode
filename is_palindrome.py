class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        max_div = 1
        x_copy = x
        while x >= 10:
            x = x / 10
            max_div *= 10
        if max_div < 10:
            return True
        while x_copy > 0:
            t = x_copy % 10
            h = x_copy / max_div
            if t != h:
                return False
            x_copy = (x_copy - h * max_div) / 10
            max_div /= 100
        return True

print Solution().isPalindrome(10)