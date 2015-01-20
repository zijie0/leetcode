class Solution:
    # @return an integer
    def atoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = s.strip()
        if not s:
            return 0
        result, init_len = '', 0

        if s[0] in '+-':
            result += s[0]
            init_len = 1

        for c in s[init_len:]:
            if 48 <= ord(c) <= 57:
                result += c
            else:
                break
        if len(result) > init_len:
            result = int(result)
        else:
            return 0
        if result > INT_MAX:
            result = INT_MAX
        elif result < INT_MIN:
            result = INT_MIN
        return result

print Solution().atoi("1")