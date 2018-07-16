class Solution:
    def SearchInsert(self,A,target):
        start,end=0,len(A)-1
        while start<end:
            mid=(start+end)//2
            if A[start]==target:
                return start
            elif A[end]==target:
                return end
            else:
                if A[mid]==target:
                    return mid
                elif A[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
        return 0
#Test Case:
sol=Solution()
print(sol.SearchInsert([1,3,5,6],1))
