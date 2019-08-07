class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        left,right=0,len(A)-1
        while left<right-1:
            mid=(left+right)//2
            if A[mid]<A[mid+1]:
                left=mid
            else:
                right=mid
        if A[left]<A[right]:
            return right
        else:
            return left
sol=Solution()
print(sol.findPeak([13,20,21,17]))
