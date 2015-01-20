class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        total_len = len(A)
        if total_len <= 1:
            return total_len
        i, j = 1, 1
        while i < total_len:
            if A[i] != A[i-1]:
                A[j] = A[i]
                j += 1
            i += 1
        return j

print Solution().removeDuplicates([1,1,2,3])