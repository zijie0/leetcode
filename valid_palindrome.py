import re

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        s = re.sub(r'\W+', '', s.lower())
        print s
        rev_s = s[::-1]
        if s == rev_s:
            return True
        else:
            return False

print Solution().isPalindrome("A man, a plan, a canal: Panama")