class Solution:
    # @return a boolean
    def isValid(self, s):
        check = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                if not stack:
                    return False
                if check[stack.pop()] != c:
                    return False
        if stack:
            return False
        return True

print Solution().isValid(']')