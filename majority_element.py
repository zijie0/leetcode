class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        length = len(num)
        majority_num = length / 2 if length % 2 == 0 else length / 2 + 1
        cnt = dict()
        for n in num:
            cnt.setdefault(n, 0)
            cnt[n] += 1
            if cnt[n] >= majority_num:
                return n

print Solution().majorityElement([6,5,5])