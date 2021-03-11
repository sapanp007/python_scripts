s=['red', 'rose', 'rambo']


class Solution:
    @staticmethod
    def longest_common_prefix(self, s) -> str:
        if len(s) == 0:
            return ""
        cmn = s[0]
        s = s[1:]
        for i in s:
            while i.find(cmn) != 0:
                cmn = cmn[0:len(cmn)-1]
        return cmn


obj1=Solution()
print(obj1.longest_common_prefix(s))