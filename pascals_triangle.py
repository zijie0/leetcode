class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        if not numRows:
            return result
        for i in range(1, numRows+1):
            r = [None] * i
            r[0] = 1
            r[-1] = 1
            if i <= 2:
                result.append(r)
                continue
            for j in range(1, i-1):
                r[j] = result[i-2][j-1] + result[i-2][j]
            result.append(r)
        return result

print Solution().generate(4)