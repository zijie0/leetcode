class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0
        i, j = 0, 0
        total_len = len(A)
        while i < total_len:
            if A[i] != elem:
                A[j] = A[i]
                j += 1
            i += 1
        print A
        return j

print Solution().removeElement([1,1,2,3], 1)

class Solution2:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        while A.count(elem) != 0:
            A.remove(A[A.index(elem)])
        return len(A)