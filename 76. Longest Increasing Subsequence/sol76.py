class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)
        res=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]  and res[i]<res[j]+1:
                    res[i]+=1
        return max(res)
sol=Solution()
lst=[ 2, 5, 3, 7, 11, 8, 10, 13,3,4,5,6,7,8,9,1,10]
print(sol.longestIncreasingSubsequence(lst))

