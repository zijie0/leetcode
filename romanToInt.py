class Solution:
    # @return an integer
    def romanToInt(self, s):
        total_len = len(s)
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        result = 0
        i = 0
        while i < total_len-1:
            if s[i] in 'IXC':
                if s[i] + s[i+1] in special:
                    result += val[s[i+1]] - val[s[i]]
                    i += 2
                else:
                    result += val[s[i]]
                    i += 1
            else:
                result += val[s[i]]
                i += 1
        if i < total_len:
            result += val[s[i]]
        return result

print Solution().romanToInt('MCMXCVI')