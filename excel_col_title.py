import math

class Solution:
    # @return a string
    def convertToTitle(self, num):
        length = int(math.ceil(math.log(num * 25 + 26) / math.log(26))) - 1
        base = ord('A')
        result = ''
        for i in range(length, 0, -1):
            last_max = (26 ** i - 26) / 25
            coef = int(math.ceil(float(num - last_max) / 26 ** (i-1)))
            result += chr(coef + base - 1)
            num -= 26 ** (i-1) * coef
        return result

class Solution2:
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)