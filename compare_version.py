class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        version1 = [int(x) for x in version1.split('.')]
        version2 = [int(x) for x in version2.split('.')]
        length1 = len(version1)
        length2 = len(version2)
        i = 0
        while True:
            if i < length1 and i < length2:
                if version1[i] < version2[i]:
                    return -1
                elif version1[i] > version2[i]:
                    return 1
                else:
                    i += 1
            elif i >= length1 and i < length2:
                if version2[i] > 0:
                    return -1
                else:
                    i += 1
            elif i >= length2 and i < length1:
                if version1[i] > 0:
                    return 1
                else:
                    i += 1
            else:
                return 0

print Solution().compareVersion('1', '1.0')
