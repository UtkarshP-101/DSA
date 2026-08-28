class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre=strs[0]
        for a in strs:
            i=0
            while i<len(pre) and i<len(a):
                if pre[i]!=a[i]:
                    break
                i+=1
            pre=pre[0:i]
        return pre