class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        min_len, min_str = float("inf"), None
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
                min_str = s
        idx = 0
        while idx < min_len:
            c = min_str[idx]
            for s in strs:
                if s[idx] != c:
                    return min_str[:idx]
            idx += 1
        return min_str[:idx]

class Solution2:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

print Solution().longestCommonPrefix(['abc'])