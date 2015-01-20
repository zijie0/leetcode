class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        row = []
        if rowIndex < 0:
            return row
        for i in range(rowIndex+1):
            row = [None] * (i + 1)
            row[0] = 1
            row[-1] = 1
            if i < 2:
                last = row
                continue
            for j in range(1, i):
                row[j] = last[j-1] + last[j]
            last = row
        return row

print Solution().getRow(0)