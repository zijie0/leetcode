class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if not s:
            return 0
        length = len(s)
        result = 0
        for c in s:
            result += (ord(c) - ord('A') + 1) * 26 ** (length - 1)
            length -= 1
        return result


print Solution().titleToNumber('BZ')