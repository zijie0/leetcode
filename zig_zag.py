class Solution:
    # @return a string
    def convert(self, s, nRows):
        total_len = len(s)
        if nRows < 2 or total_len <= nRows:
            return s

        zig_len = nRows * 2 - 2
        result = ''
        for r in range(nRows):
            z = 0
            while True:
                zig = zig_len * z + r
                if zig >= total_len:
                    break
                result += s[zig]
                if r > 0 and r < nRows - 1:
                    zag = zig + (nRows - 1 - r) * 2
                    if zag < total_len:
                        result += s[zag]
                z += 1
        return result

print Solution().convert("ABCD", 3)