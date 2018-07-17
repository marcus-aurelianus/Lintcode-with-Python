class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        start,end=0,len(A)-1
        while start<=end:
            mid=(start+end)//2
            print(A[start],A[mid],A[end],target)
            if A[start]==target:
                return start
            elif A[end]==target:
                return end
            else:
                if A[mid]==target:
                    return mid
                elif A[mid]>target:
                    if A[start]<A[mid]:
                        if A[start]<target:
                            start,end=start+1,mid-1 
                        else:
                            start,end=mid+1,end-1
                    else:
                        if A[end]>target:
                            start,end=start+1,mid-1 
                        else:
                            start,end=mid+1,end-1
                else:
                    if A[end]>target:
                        start,end=mid+1,end-1
                    else:
                        start,end=start+1,mid-1
        return -1

#Test Case:
sol=Solution()
print(sol.search([1001,10001,10007,1,10,101,201],1001))
