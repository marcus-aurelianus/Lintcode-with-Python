class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        left,right=1,n
        while left<=right-1:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid
            else:
                left=mid
        return left
            
