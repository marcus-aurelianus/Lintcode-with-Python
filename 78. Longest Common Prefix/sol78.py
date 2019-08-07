class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        mins=min((strs))
        maxs=max((strs))
        pre=""
        for i in range(min(len(mins),len(maxs))):
            if (mins[i]==maxs[i]):
                pre=pre+mins[i]
            else:
                break
        return pre
sol=Solution()
print(sol.longestCommonPrefix(["ABCD", "ADEF", "ACEF","ABCDEF"]))
